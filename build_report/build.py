import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from build_report.helpers import set_cell_margins, set_cell_borders
from build_report.preliminary import (
    add_cover_page, add_certificate, add_declaration, add_acknowledgement,
    add_abstract, add_table_of_contents, add_list_of_figures, add_list_of_tables,
    add_list_of_abbreviations
)
from build_report.chapter1 import add_chapter_1
from build_report.chapter2 import add_chapter_2
from build_report.chapter3 import add_chapter_3
from build_report.chapter4 import add_chapter_4
from build_report.chapter5 import add_chapter_5
from build_report.chapter6 import add_chapter_6
from build_report.chapter7 import add_chapter_7
from build_report.references_appendix import add_references_and_appendix

def setup_page_geometry(section):
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.left_margin = Inches(1.5)
    section.right_margin = Inches(1.0)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)

def main():
    print("=== BUILDING MINI PROJECT REPORT ===")
    doc = docx.Document()

    # SECTION 1: Preliminary Pages (No Header, No Footer)
    s1 = doc.sections[0]
    setup_page_geometry(s1)

    print("Adding Cover Page...")
    add_cover_page(doc)

    print("Adding Certificate...")
    add_certificate(doc)

    print("Adding Declaration...")
    add_declaration(doc)

    print("Adding Acknowledgement...")
    add_acknowledgement(doc)

    print("Adding Abstract...")
    add_abstract(doc)

    print("Adding Table of Contents...")
    add_table_of_contents(doc)

    print("Adding List of Figures...")
    add_list_of_figures(doc)

    print("Adding List of Tables...")
    add_list_of_tables(doc)

    print("Adding List of Abbreviations...")
    add_list_of_abbreviations(doc)

    # SECTION 2: Chapter Pages Onward (Header and Footer Active)
    print("Configuring Section 2 (Chapter Pages Onward)...")
    s2 = doc.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    setup_page_geometry(s2)

    # Unlink headers and footers from Section 1
    s2.header.is_linked_to_previous = False
    s2.footer.is_linked_to_previous = False

    # Reset page numbering to start at 1 in Section 2
    pgNumType = parse_xml(f'<w:pgNumType {nsdecls("w")} w:start="1"/>')
    s2._sectPr.append(pgNumType)

    # HEADER: Right-aligned "Mini Project Report"
    hp = s2.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("Mini Project Report")
    hrun.font.name = 'Times New Roman'
    hrun.font.size = Pt(10)
    hrun.font.italic = True
    hrun.font.color.rgb = RGBColor(113, 128, 150)

    # FOOTER: Center-aligned Department Name + Right-aligned Page Number
    tbl = s2.footer.add_table(1, 3, Inches(5.77))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in tbl.rows:
        for cell in r.cells:
            set_cell_margins(cell, top=60, bottom=60, left=40, right=40)
            set_cell_borders(cell, top="none", bottom="none", left="none", right="none")

    c0, c1, c2 = tbl.rows[0].cells
    c0.width = Inches(1.0)
    c1.width = Inches(3.77)
    c2.width = Inches(1.0)

    # Center cell: Department Name
    p_dept = c1.paragraphs[0]
    p_dept.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_dept = p_dept.add_run("Department of Computer Science & Engineering")
    r_dept.font.name = 'Times New Roman'
    r_dept.font.size = Pt(9)
    r_dept.font.color.rgb = RGBColor(113, 128, 150)

    # Right cell: Page Number (PAGE field)
    p_num = c2.paragraphs[0]
    p_num.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_num = p_num.add_run()
    r_num.font.name = 'Times New Roman'
    r_num.font.size = Pt(9.5)
    r_num.font.color.rgb = RGBColor(45, 55, 72)
    fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>')
    fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>')
    fldChar3 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    r_num._r.append(fldChar1)
    r_num._r.append(instrText)
    r_num._r.append(fldChar2)
    r_num._r.append(fldChar3)

    # ADD CHAPTERS
    print("Adding Chapter 1...")
    add_chapter_1(doc)

    print("Adding Chapter 2...")
    doc.add_page_break()
    add_chapter_2(doc)

    print("Adding Chapter 3...")
    doc.add_page_break()
    add_chapter_3(doc)

    print("Adding Chapter 4...")
    doc.add_page_break()
    add_chapter_4(doc)

    print("Adding Chapter 5...")
    doc.add_page_break()
    add_chapter_5(doc)

    print("Adding Chapter 6...")
    doc.add_page_break()
    add_chapter_6(doc)

    print("Adding Chapter 7...")
    doc.add_page_break()
    add_chapter_7(doc)

    print("Adding References & Appendix...")
    doc.add_page_break()
    add_references_and_appendix(doc)

    # Output paths
    out_docx = os.path.abspath("presentation/Mini_Project_Report_Dev_Rana_Kaila.docx")
    out_pdf = os.path.abspath("presentation/Mini_Project_Report_Dev_Rana_Kaila.pdf")

    print(f"Saving Word Document: {out_docx}...")
    doc.save(out_docx)
    print("DOCX saved successfully!")

    # Convert to PDF via MS Word
    print("Converting DOCX to PDF via MS Word...")
    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        try:
            doc_word = word.Documents.Open(out_docx)
            doc_word.SaveAs(out_pdf, FileFormat=17) # 17 = wdFormatPDF
            doc_word.Close()
            print(f"PDF exported successfully to: {out_pdf}!")
        finally:
            word.Quit()
    except Exception as e:
        print(f"Word PDF conversion failed: {e}")

if __name__ == "__main__":
    main()
