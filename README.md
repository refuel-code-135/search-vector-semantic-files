# semantic-file-search

```
conda create -n semantic-file-search python=3.10
conda activate semantic-file-search

pip install \
  jupyterlab \
  pandas \
  numpy \
  sentence-transformers \
  faiss-cpu \
  python-docx \
  openpyxl \
  pdfplumber \
  pycln \
  isort \
  black

#  PyMuPDF
```

```
pycln . && isort . --profile=black && black .
```
