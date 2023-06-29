import PyPDF4


def extract_links_from_pdf(file_path):
    links = []
    with open(file_path, 'rb') as file:
        pdf = PyPDF4.PdfFileReader(file)
        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            annotations = page.get('/Annots')
            if annotations:
                for annotation in annotations:
                    if isinstance(annotation, PyPDF4.generic.IndirectObject):
                        # Handle IndirectObject type
                        annotation = pdf.getObject(annotation)
                    if annotation.get('/A'):
                        link = annotation['/A']['/URI']
                        links.append(link)

    if not links:
        raise ValueError("Файл пустой или не содержит ссылок")

    return links
