from ast import parse
from pdf2docx import parse
from pdf2_docx import Converter


pdf_file = 'settlin.pdf'
docx_file = 'settlin.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

# #Alternative, Using the parse method

# pdf_file = '/home/safety/Python-Projects/Automation/auto_projc/settlin.pdf'
# docx_file = '/home/safety/Python-Projects/Automation/auto_projc/settlin1.docx'

# #convert pdf to docx
# parse(pdf_file, docx_file)