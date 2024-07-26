from PyPDF2 import PdfMerger

def by_appending():
    merger = PdfMerger()
    with open("testPDF1.pdf", "rb") as f1:
        merger.append(f1)
    merger.append("testPDF2.pdf")
    merger.write("mergedPDF_appending.pdf")
    merger.close()

def by_inserting():
    merger = PdfMerger()
    merger.append("testPDF1.pdf")
    merger.merge(0, "testPDF2.pdf")
    merger.write("mergedPDF_inserting.pdf")
    merger.close()

if __name__ == "__main__":
    by_appending()
    by_inserting()
