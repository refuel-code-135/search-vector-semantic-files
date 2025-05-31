import numpy as np
from sentence_transformers import SentenceTransformer

# モデル読み込み（日本語対応のものも可）
# 例: 'intfloat/multilingual-e5-small' は軽量かつ日本語対応
model = SentenceTransformer("intfloat/multilingual-e5-small")


def embed_chunks(chunks):
    """
    chunkのリスト（textを含む辞書）をベクトル化して返す

    Args:
        chunks (List[Dict]): 各チャンクに"text"キーが含まれる必要あり

    Returns:
        List[Dict]: "embedding"（np.ndarray）を追加した辞書のリスト
    """
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts, normalize_embeddings=True)

    # 各チャンクに埋め込みを追加
    for chunk, emb in zip(chunks, embeddings):
        chunk["embedding"] = emb  # numpy配列

    return chunks
