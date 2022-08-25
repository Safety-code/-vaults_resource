import PyPDF2

# Open the pdf file and create writer object
pdfFile = open("chapter2.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through the pages and add the pages to the writer object
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
    
# Encrypt the file into a new Pdf file and provide password     
pdfWriter.encrypt('safety')
resultingPDF = open("chapter2_encrypted.pdf", "wb")
resultingPDF.close()
