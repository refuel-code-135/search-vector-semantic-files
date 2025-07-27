# demo.py
import pickle

import faiss
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer

st.title("File Server Semantic Search")

# Input query
query = st.text_input("Enter your question or topic:")

if query:
    # Load embedding model and FAISS index
    model = SentenceTransformer("intfloat/multilingual-e5-small")
    index = faiss.read_index("data/faiss/faiss.index")

    with open("data/faiss/faiss_meta.pkl", "rb") as f:
        chunks = pickle.load(f)

    # Encode query and search FAISS index
    vec = model.encode([query], normalize_embeddings=True).astype("float32")
    k = 5
    D, I = index.search(vec, k)  # D: distances, I: indices

    # Format and sort results by similarity
    results = []
    for idx, dist in zip(I[0], D[0]):
        if idx < len(chunks):
            results.append(
                {
                    "score": float(dist),
                    "file_path": chunks[idx]["file_path"],
                    "page": chunks[idx].get(
                        "page", "?"
                    ),  # fallback to "?" if not available
                    "text": chunks[idx]["text"][:150] + "...",
                }
            )
    results.sort(key=lambda x: x["score"])

    # Display results
    st.subheader("Top 5 Results:")
    for res in results:
        st.markdown("---")
        st.write(f"**{res['file_path']} (Page {res['page']})**")
        st.write(f"Similarity Score (L2 distance): `{res['score']:.4f}`")
        st.text(res["text"])
