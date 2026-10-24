import fitz

doc = fitz.open('presentation/Mini_Project_Report_Dev_Rana_Kaila.pdf')
print(f"Total Pages: {len(doc)}")

chapters = [
    'CERTIFICATE', 'DECLARATION', 'ACKNOWLEDGEMENT', 'ABSTRACT', 
    'TABLE OF CONTENTS', 'LIST OF FIGURES', 'LIST OF TABLES', 'LIST OF ABBREVIATIONS',
    'CHAPTER 1: INTRODUCTION', 'CHAPTER 2: LITERATURE REVIEW', 
    'CHAPTER 3: SYSTEM ANALYSIS', 'CHAPTER 4: IMPLEMENTATION', 
    'CHAPTER 5: TESTING', 'CHAPTER 6: RESULTS AND DISCUSSION', 
    'CHAPTER 7: CONCLUSION', 'REFERENCES', 'APPENDIX'
]

for p in range(len(doc)):
    txt = doc[p].get_text()
    for ch in chapters:
        if ch in txt and 'TABLE OF CONTENTS' not in txt:
            print(f"Page {p+1:02d}: {ch}")
            chapters.remove(ch)
            break
