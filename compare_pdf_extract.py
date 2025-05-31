from pathlib import Path

import fitz  # PyMuPDF
import pdfplumber


def extract_with_pymupdf(file_path):
    print("🟢 PyMuPDF (fitz) 抽出結果")
    doc = fitz.open(file_path)
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        print(f"\n--- Page {i+1} ---")
        print(text[:500])  # 最初の500文字だけ表示
    print("\n" + "=" * 60 + "\n")


def extract_with_pdfplumber(file_path):
    print("🔵 pdfplumber 抽出結果")
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            print(f"\n--- Page {i+1} ---")
            print(text[:500] if text else "[NO TEXT]")
    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    pdf_file = Path("data/sample.pdf")
    assert pdf_file.exists(), f"{pdf_file} が見つかりません"

    extract_with_pymupdf(str(pdf_file))
    extract_with_pdfplumber(str(pdf_file))
