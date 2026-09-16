import os
import argparse
import json
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm

# We will create mock implementations if these are not yet defined, but the project requires importing them
try:
    from src.models.dual_stream_net import DualStreamNet
except ImportError:
    # Dummy implementation so the script is runnable
    class DualStreamNet(nn.Module):
        def __init__(self):
            super().__init__()
            self.fc = nn.Linear(3 * 256 * 256, 1)
        def forward(self, x_rgb, x_dct):
            x = x_rgb.view(x_rgb.size(0), -1)
            return self.fc(x)

try:
    from src.data.dct_transform import DCTTransform
except ImportError:
    class DCTTransform:
        def __call__(self, img):
            return torch.zeros((1, 256, 256))

try:
    from config import Config
except ImportError:
    class Config:
        DATA_DIR = 'data'
        BATCH_SIZE = 16
        EPOCHS = 20

from src.data.dataset import DeepfakeDataset, create_demo_dataset
from src.data.augmentation import get_train_transforms, get_val_transforms
from src.utils.metrics import compute_all_metrics, MetricTracker

def train_one_epoch(model, loader, criterion, optimizer, scaler, device):
    model.train()
    losses = MetricTracker()
    all_targets = []
    all_scores = []
    
    pbar = tqdm(loader, desc="Training")
    for batch in pbar:
        images = batch['image'].to(device)
        dcts = batch['dct'].to(device)
        targets = batch['label'].to(device).unsqueeze(1)
        
        optimizer.zero_grad()
        
        with torch.cuda.amp.autocast(enabled=scaler.is_enabled()):
            output_dict = model(images, dcts)
            logits = output_dict['logits']
            loss = criterion(logits, targets)
            
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
        
        losses.update(loss.item(), images.size(0))
        
        scores = output_dict['probs'].detach().cpu().numpy()
        all_targets.extend(targets.cpu().numpy())
        all_scores.extend(scores)
        
        pbar.set_postfix({'loss': f'{losses.avg:.4f}'})
        
    metrics = compute_all_metrics(all_targets, all_scores)
    metrics['loss'] = losses.avg
    return metrics

@torch.no_grad()
def validate(model, loader, criterion, device):
    model.eval()
    losses = MetricTracker()
    all_targets = []
    all_scores = []
    
    pbar = tqdm(loader, desc="Validation")
    for batch in pbar:
        images = batch['image'].to(device)
        dcts = batch['dct'].to(device)
        targets = batch['label'].to(device).unsqueeze(1)
        
        output_dict = model(images, dcts)
        logits = output_dict['logits']
        loss = criterion(logits, targets)
        
        losses.update(loss.item(), images.size(0))
        
        scores = output_dict['probs'].cpu().numpy()
        all_targets.extend(targets.cpu().numpy())
        all_scores.extend(scores)
        
    metrics = compute_all_metrics(all_targets, all_scores)
    metrics['loss'] = losses.avg
    return metrics

def main():
    parser = argparse.ArgumentParser(description="Dual-Stream Deepfake Detection Training")
    parser.add_argument('--data_dir', type=str, default='dataset', help='Path to dataset')
    parser.add_argument('--epochs', type=int, default=20, help='Number of epochs')
    parser.add_argument('--batch_size', type=int, default=16, help='Batch size')
    parser.add_argument('--lr', type=float, default=1e-4, help='Learning rate')
    parser.add_argument('--output_dir', type=str, default='outputs', help='Output directory')
    args = parser.parse_args()
    
    os.makedirs(args.output_dir, exist_ok=True)
    
    if not os.path.exists(args.data_dir):
        print(f"Dataset not found at {args.data_dir}. Creating demo dataset...")
        create_demo_dataset(args.data_dir)
        
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    train_transform = get_train_transforms()
    val_transform = get_val_transforms()
    dct_transform = DCTTransform()
    
    train_dataset = DeepfakeDataset(args.data_dir, split='train', transform=train_transform, dct_transform=dct_transform)
    val_dataset = DeepfakeDataset(args.data_dir, split='val', transform=val_transform, dct_transform=dct_transform)
    
    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, num_workers=4 if torch.cuda.is_available() else 0, drop_last=True)
    val_loader = DataLoader(val_dataset, batch_size=args.batch_size, shuffle=False, num_workers=4 if torch.cuda.is_available() else 0)
    
    model = DualStreamNet().to(device)
    
    criterion = nn.BCEWithLogitsLoss(pos_weight=torch.tensor([1.0]).to(device))
    optimizer = optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingWarmRestarts(optimizer, T_0=10, eta_min=1e-6)
    
    scaler = torch.cuda.amp.GradScaler(enabled=device.type=='cuda')
    
    best_auc = 0.0
    patience_counter = 0
    patience = 6
    history = {'train': [], 'val': []}
    
    for epoch in range(args.epochs):
        print(f"\nEpoch {epoch+1}/{args.epochs}")
        
        train_metrics = train_one_epoch(model, train_loader, criterion, optimizer, scaler, device)
        val_metrics = validate(model, val_loader, criterion, device)
        
        scheduler.step()
        
        history['train'].append(train_metrics)
        history['val'].append(val_metrics)
        
        print(f"Train - Loss: {train_metrics['loss']:.4f}, AUC: {train_metrics['auc_roc']:.4f}, Acc: {train_metrics['accuracy']:.4f}")
        print(f"Val   - Loss: {val_metrics['loss']:.4f}, AUC: {val_metrics['auc_roc']:.4f}, Acc: {val_metrics['accuracy']:.4f}")
        
        if val_metrics['auc_roc'] > best_auc:
            best_auc = val_metrics['auc_roc']
            patience_counter = 0
            torch.save(model.state_dict(), os.path.join(args.output_dir, 'best_model.pth'))
            print("=> Saved new best model")
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print(f"Early stopping triggered after {epoch+1} epochs")
                break
                
    with open(os.path.join(args.output_dir, 'training_history.json'), 'w') as f:
        json.dump(history, f, indent=4)
        
    print("\nTraining Complete!")
    print(f"Best Validation AUC-ROC: {best_auc:.4f}")

if __name__ == '__main__':
    main()
