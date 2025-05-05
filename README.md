# 🐔 Chicken Disease Classification - Coccidiosis Detection

This repository presents a deep learning-based solution for detecting **Coccidiosis**, a common chicken disease, using image classification techniques. The project leverages a Convolutional Neural Network (CNN) to identify whether a chicken is **infected** or **healthy** based on fecal image samples.

---

## 🚀 Features

- ✅ Automatic classification of chicken fecal images (Healthy vs Coccidiosis)
- 🧠 Deep learning with transfer learning
- 🌐 Flask-based web app for real-time predictions - TODO
- 📦 Dockerized for consistent deployment - TODO
- ⏱️ GitHub Actions for CI/CD - TODO
- 🧪 DVC for experiment & data tracking - TODO

---

## 📂 Project Structure

```
├── artifacts/            # Saved artifacts like models, processed data, etc.
├── src/                  # Source code for components
├── templates/            # HTML templates for Flask app
├── static/               # Static files (CSS, JS, images)
├── config/               # YAML config files for params and settings
├── app.py                # Flask app
├── requirements.txt      # Project dependencies
├── Dockerfile            # Docker instructions
├── .github/workflows/    # GitHub Actions for CI/CD
└── README.md             # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rohith05196/Chicken-Disease-Classification.git
cd Chicken-Disease-Classification
```

### 2. Create & Activate Virtual Environment

```bash
conda create -p venv python=3.8 -y
conda activate venv/
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
