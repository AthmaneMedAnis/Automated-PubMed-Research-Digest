from fpdf import FPDF
import pandas as pd
from os import path

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'PubMed Research Digest', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def clean_text(text):
    """
    FPDF (standard) struggles with some Unicode characters (emojis, math symbols).
    This function converts text to Latin-1 compatible format to prevent crashes.
    """
    if not text:
        return ""
    return str(text).encode('latin-1', 'replace').decode('latin-1')

def generate_pdf(df: pd.DataFrame, query: str, image_path: str, output_pdf_path: str):    
    pdf = PDFReport()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Search Query: {clean_text(query)}", ln=1, align='C')
    pdf.cell(200, 10, txt=f"Total Papers Found: {len(df)}", ln=1, align='C')
    
    if path.exists(image_path):
        pdf.image(image_path, x=10, y=40, w=190)
    else:
        pdf.ln(20)

    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Top Papers", ln=1)
    
    for index, row in df.iterrows():
        pdf.set_font("Arial", "B", 11)
        pdf.multi_cell(0, 8, clean_text(row.get('Title', 'No Title')))
        
        pdf.set_font("Arial", "I", 9)
        meta = f"{row.get('Journal', 'Unknown Journal')} | {row.get('Date of Publication', 'No Date')}"
        pdf.cell(0, 6, clean_text(meta), ln=1)
        
        pdf.set_font("Arial", size=9)
        abstract = row.get('Abstract', '')
        if len(abstract) > 500:
            abstract = abstract[:500] + " [...]"
        
        pdf.multi_cell(0, 5, clean_text(abstract))
        
        pdf.ln(5)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
        
        if pdf.get_y() > 250:
            pdf.add_page()

    pdf.output(output_pdf_path)