from fpdf import FPDF

#creating a pdf:

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
pdf.text(10,10,"Isaias Souza")

pdf.output("MyFirst.pdf")
