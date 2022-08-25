import PyPDF2
import os

# combinePdfs.py - Combines allt the PDFS in the #current working directory into a single PDF.

# Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(str.lower, key=filename)

pdfWriter = PyPDF2.PdfFileWriter()

#Loop through all the PDF files

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# Loop through all the pages (except the frst) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file
pdfoutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfoutput)
pdfoutput.close()
