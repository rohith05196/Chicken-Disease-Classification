import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'clasifier_cnn'

list_of_base_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "templates/home.html",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in list_of_base_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    # create dirs if it doesnt exist
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating Directory named: {file_dir}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with(open(filepath, 'w')) as f:
            pass
            logging.info(f"Creating an empty file : {file_name}")
    
    else:
        logging.info(f"Creating an empty file : {file_name}")
    

