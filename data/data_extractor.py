import PyPDF2

def extract_text_from_pdf(path_file, no_pages=300):
    extracted_book_page = []
    with open(path_file, 'rb') as pdf_file:
        read_book = PyPDF2.PdfReader(pdf_file)
        for i in range(no_pages):
            all_pages = read_book.pages[i]
            extracting_text = all_pages.extract_text()
            if extracting_text:
                extracting_text = extracting_text.replace('-\n', '').replace('\n', ' ')
                extracted_book_page.append(extracting_text)
    extracted_text = ''.join(extracted_book_page)
    return extracted_text

