import os
from pathlib import Path

list_of_files = [
    
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/document_loader.py",
    "src/components/text_splitter.py",
    "src/components/vectorstore.py",
    "src/components/retrieval.py",
    "src/components/generation.py",
    "src/components/chain.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exceptions/exception.py",
    "requirements.txt",
    "setup.py",
    "experiment/experiments.ipynb"
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        # logging.info(f"Creating directory: {filedir} for file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file