from docx import Document
from docxtpl import DocxTemplate
from docx.shared import Pt
from docx.shared import Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import docxtpl
import csv

try:
    file = open("4/data_marathon.csv")
except FileNotFoundError:
    exit("File not found.")
reader = csv.reader(file)
sortedlist = sorted(reader, key=lambda row:(row[0],row[5]), reverse=False)
doc = Document()

unique_years = 0
counter = 0
for i in range(1, len(sortedlist)):
    if sortedlist[i-1][0] != sortedlist[i][0] or sortedlist[i-1][5] != sortedlist[i][5]:
        counter = 0
        unique_years += 1
        doc.add_page_break()
    # print(sortedlist[i])
    counter += 1
    doc.add_paragraph("{{subdoc" + str(unique_years) + "_" + str(counter) + "}}")

doc.save('4/result2.docx')

unique_years = 0
counter = 0
context = {}
for i in range(1, len(sortedlist)):
    if sortedlist[i-1][0] != sortedlist[i][0] or sortedlist[i-1][5] != sortedlist[i][5]:
        counter = 0
        unique_years += 1
    counter += 1
    context["subdoc" + str(unique_years) + "_" + str(counter)] = "f"

doc = DocxTemplate("4/result2.docx")
doc.render(context)
doc.save("4/generated_docx.docx")