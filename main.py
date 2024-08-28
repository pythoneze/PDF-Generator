from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

def create_header(topic):
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1)

def create_footer(topic):
    pdf.set_y(-10) 
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 180, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

def create_lines(y_position):
    pdf.line(10, y_position, 200, y_position)

for _, row in df.iterrows():
    # Header
    pdf.add_page()
    create_header(row["Topic"])
    for y in range(20, 290, 10):        
        create_lines(y)

    create_footer(row["Topic"])

    for _ in range(row["Pages"] - 1):
        pdf.add_page()
        for y in range(20, 290, 10):        
            create_lines(y)
        create_footer(row["Topic"])

pdf.output("output.pdf")