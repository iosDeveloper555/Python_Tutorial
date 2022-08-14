import PyPDF2
import os

resorces_path = "/Users/apple/Documents/Python/PyCharm_Project/Python_Scripting/Resources/PDFS"

template = PyPDF2.PdfFileReader(open((resorces_path+"/super.pdf"), "rb"))
watermark = PyPDF2.PdfFileReader(open((resorces_path+"/watermark.pdf"), "rb"))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open((resorces_path+"/watermark_output.pdf"),"wb") as file:
        output.write(file)



''' # Combine  pdf

def pdf_combiner(pdf_list):
    print(pdf_list)
    merger = PyPDF2.PdfFileMerger()
    for pdf in os.listdir(pdf_list):
        print(pdf)
        merger.append(resorces_path+"/"+pdf)
    merger.write((resorces_path+"/super.pdf"))

pdf_combiner(resorces_path)

'''

'''  # Roatate PDF

try:
  with open(resorces_path+"PDFS/dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open(resorces_path+"PDFS/tilt.pdf","wb") as new_file:
        writer.write(new_file)
        print("all done!")

except FileNotFoundError as error:
    print(f"FileNotFoundError {error}")


'''
