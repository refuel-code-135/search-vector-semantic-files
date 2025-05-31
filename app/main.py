from app.chunking.pdf_chunker import chunk_pdf
from app.embedding import embed_chunks
from app.vector_store import build_faiss_index, save_faiss_index, save_metadata


def main():
    file_path = "data/sample.pdf"
    index_path = "data/faiss.index"
    meta_path = "data/faiss_meta.pkl"

    # ステップ1: PDFをチャンク化
    chunks = chunk_pdf(file_path)
    print(f"✅ チャンク数: {len(chunks)}")

    # ステップ2: チャンクをベクトル化
    embedded = embed_chunks(chunks)
    print("✅ ベクトル化完了（1件目の先頭5次元）:")
    print(embedded[0]["embedding"][:5])

    # ステップ3: FAISSインデックスを構築・保存
    index = build_faiss_index(embedded)
    save_faiss_index(index, index_path)
    save_metadata(embedded, meta_path)

    print(f"✅ FAISS保存完了 → {index_path}")
    print(f"✅ メタ情報保存完了 → {meta_path}")


if __name__ == "__main__":
    main()
