# CNN-Based Image Classification Pipeline

This repository provides an end-to-end machine learning pipeline for image classification using a Convolutional Neural Network (CNN). The system includes data versioning, model training, evaluation, prediction pipeline deployment, and Docker support.

**Note**: This project was taken up as a part of personal learning.

---

## 📁 Project Structure

```
├── .dvc/                  # DVC pipeline and stage management
├── .github/               # GitHub workflows and config
├── artifacts/             # Stores trained models and intermediate artifacts
├── config/                # Configuration files for model training
├── research/              # Research notebooks or scripts
├── run_logs/              # Logs from training or inference runs
├── src/classifier_cnn/    # Source code for CNN model and utilities
├── templates/             # HTML templates (likely for app UI)
├── tf-env/                # TensorFlow virtual environment files
├── app.py                 # Flask or FastAPI app to serve model
├── DockerFile             # Docker configuration
├── dvc.lock / dvc.yaml    # DVC pipeline specification and lock file
├── inputImage.jpg         # Sample input image
├── params.yaml            # Hyperparameters and config for training
├── requirements.txt       # Python dependencies
├── scores.json            # Model scores/metrics after evaluation
├── setup.py               # Project setup and installation
├── test_run.py            # Evaluation or inference testing script
└── README.md              # Project description and usage instructions
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```
### 2. Create & Activate Virtual Environment

```bash
conda create -p venv python=3.8 -y
conda activate venv/
```

### 3. Install Dependencies
Install required packages:
```bash
pip install -r requirements.txt
```

Or use the pre-configured virtual environment in `tf-env`.

### 4. Reproduce Pipeline with DVC
```bash
dvc repro
```

or 

### 4. run the entire model

```bash
python test_run.py
```

### 5. Run the App
```bash
python app.py
```
---

## 🧪 Features

- CNN model training with parameter configuration
- Image classification inference pipeline
- Dockerized deployment
- DVC for reproducibility
- Logs and evaluation metrics saved
- Web interface integration via `templates/`

---

## 🐳 Docker

To build and run the app in Docker:
```bash
docker build -t cnn-classifier .
docker run -p 8080:8080 cnn-classifier
```

---

## 📬 Contact

For questions or suggestions, please open an issue, I will respond to the querries at the earliest possible.
