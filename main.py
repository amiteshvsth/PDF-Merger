import PyPDF2

pdFiles = ["1.pdf", "2.pdf", "3.pdf"]
merger = PyPDF2.PdfMerger()

for filename in pdFiles:
    pdFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdFile)
    merger.append(pdfReader)
pdFile.close()
merger.write('merged.pdf')
