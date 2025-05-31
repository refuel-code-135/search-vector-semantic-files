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

```

```
pycln . && isort . --profile=black && black .
```
