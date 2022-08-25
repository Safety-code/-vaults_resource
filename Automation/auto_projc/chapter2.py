import PyPDF2

pdfFile  = open('csharp.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
readPageNum = pdfReader.numPages

pdfFile = pdfReader.getPage(33)
print(pdfFile.extract_text())
print(readPageNum)

# Looping through the pages from page 10 to 33
for pageNum in range(10, 33):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
# saving the output into a new PDF file
pdfoutput = open('chapteronly.pdf', 'wb')
pdfWriter.write(pdfoutput)
pdfoutput.close()
