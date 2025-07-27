import os
import pickle

import faiss
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer

# Set page config
st.set_page_config(page_title="File Search", layout="wide")

# Custom CSS for soft background
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
    }
    .stMetric {
        text-align: right;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("File Server Semantic Search")

# Input query
query = st.text_input(
    "Enter your question or topic:", placeholder="e.g., AI adoption in healthcare"
)

if query:
    # Load model and FAISS index
    model = SentenceTransformer("intfloat/multilingual-e5-small")
    index = faiss.read_index("data/faiss/faiss.index")
    with open("data/faiss/faiss_meta.pkl", "rb") as f:
        chunks = pickle.load(f)

    # Encode and search
    vec = model.encode([query], normalize_embeddings=True).astype("float32")
    D, I = index.search(vec, k=5)

    # Format and display results
    results = []
    for idx, dist in zip(I[0], D[0]):
        if idx < len(chunks):
            chunk = chunks[idx]
            results.append(
                {
                    "score": float(dist),
                    "file_name": os.path.basename(chunk["file_path"]),
                    "page": chunk.get("page", "?"),
                    "text": chunk["text"][:250] + "...",
                }
            )

    results.sort(key=lambda x: x["score"])

    st.subheader("Top 5 Results")
    for res in results:
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"**{res['file_name']} — Page {res['page']}**")
                st.write(res["text"])
            with col2:
                st.metric(label="L2 Distance", value=f"{res['score']:.4f}")
        st.markdown("---")
