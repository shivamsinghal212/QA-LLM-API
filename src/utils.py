from PyPDF2 import PdfReader
import io


def get_pdf_text(doc):
    pdf_file = io.BytesIO(doc)

    pdf_reader = PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)
    detected_text = ""

    for page_num in range(num_pages):
        page_obj = pdf_reader.pages[page_num]
        detected_text += page_obj.extract_text() + "\n\n"

    return detected_text
