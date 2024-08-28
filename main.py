from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for i, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(200, 10, txt=row['Topic'], ln=True)
    pdf.line(10, 18, 200, 18)

    for i in range(row["Pages"] - 1):
        pdf.add_page()


pdf.output("output.pdf")