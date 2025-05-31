# demo.py
import streamlit as st
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

st.title("自然文ファイル検索デモ")

query = st.text_input("キーワードを入力してください")
if query:
    # モデル & データ読み込み
    model = SentenceTransformer("intfloat/multilingual-e5-small")
    index = faiss.read_index("notebooks/data/faiss.index")
    with open("notebooks/data/faiss_meta.pkl", "rb") as f:
        chunks = pickle.load(f)

    # クエリベクトル化 & 検索
    vec = model.encode([query], normalize_embeddings=True).astype("float32")
    k = 5
    D, I = index.search(vec, k)

    # 結果を整形してソート（距離の昇順 = 類似度が高い順）
    results = []
    for idx, dist in zip(I[0], D[0]):
        if idx < len(chunks):
            results.append({
                "score": float(dist),
                "file_path": chunks[idx]["file_path"],
                "text": chunks[idx]["text"][:150] + "..."  # 長すぎると省略
            })
    results.sort(key=lambda x: x["score"])

    # 表示
    st.subheader("検索結果（Top 5）:")
    for res in results:
        st.markdown("---")
        st.write(f"**{res['file_path']}**")
        st.write(f"類似スコア（L2距離）: `{res['score']:.4f}`")
        st.text(res["text"])

