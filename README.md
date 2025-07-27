# search-vector-semantic-files

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

```
pycln . && isort . --profile=black && black .
```

```
streamlit run demo.py
```
