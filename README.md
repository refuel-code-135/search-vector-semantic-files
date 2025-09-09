# search-vector-semantic-files

## overview

This notebook demonstrates a simple end-to-end pipeline for converting PDF documents into searchable vector representations using FAISS and multilingual sentence embeddings.

Workflow:
- Extract text from PDF files
- Generate sentence embeddings with a multilingual model
- Store vectors in a FAISS index
- Perform semantic search using a natural language query

## Notebook

https://github.com/refuel-code-135/search-vector-semantic-files/blob/main/notebooks/notebook.ipynb

## Screenshot (demo.py)
<img width="951" height="708" alt="image" src="https://github.com/user-attachments/assets/ff4b10a7-8105-4a45-bdc0-67af134587d7" />


## Set Up Analysis environment
```bash
export CONDA_ENV=search-vector-semantic-files

# Create and activate a new conda environment
conda create -n $CONDA_ENV python=3.12
conda activate $CONDA_ENV

# Install required Python packages
pip install -r requirements.txt

# Start notebook
jupyter lab
```

## Demo
```
streamlit run demo.py
```

