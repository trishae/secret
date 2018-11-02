from PyPDF2 import PdfFileReader
from constants import O_FILE
from constants import M_FILE

pdf_toread = PdfFileReader(open("./resources/"+M_FILE, "rb"))
pdf_info = pdf_toread.getDocumentInfo()
print(str(pdf_info))