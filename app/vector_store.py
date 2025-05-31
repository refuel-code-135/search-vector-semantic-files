import pickle

import faiss
import numpy as np


def build_faiss_index(embedded_chunks):
    """
    FAISSのインデックスを作成し、ベクトルを登録する
    """
    embeddings = np.array([chunk["embedding"] for chunk in embedded_chunks]).astype(
        "float32"
    )

    # ★ ここで自動的に次元を取得する
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index


def save_faiss_index(index, index_path):
    """
    FAISSインデックスをローカルファイルに保存
    """
    faiss.write_index(index, str(index_path))


def save_metadata(chunks, meta_path):
    """
    FAISSと別に、メタ情報（text, page, path など）を保存
    """
    for chunk in chunks:
        chunk["embedding"] = None  # メタ情報だけ保存（軽量化）

    with open(meta_path, "wb") as f:
        pickle.dump(chunks, f)
