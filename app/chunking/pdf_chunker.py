import pdfplumber

def chunk_pdf(file_path):
    chunks = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                chunks.append({
                    "chunk_id": f"{file_path}_page_{i+1}",
                    "text": text.strip(),
                    "page": i + 1,
                    "file_path": file_path
                })
    return chunks

