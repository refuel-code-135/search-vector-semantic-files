# semantic-file-search

```
conda create -n semantic-file-search python=3.10
conda activate semantic-file-search

pip install \
  jupyterlab \
  pandas \
  numpy \
  seaborn \
  sentence-transformers \
  faiss-cpu \
  python-docx \
  openpyxl \
  pdfplumber \
  pycln \
  isort \
  black

pip install streamlit


```

```
pycln . && isort . --profile=black && black .
```

```
streamlit run demo.py
```
