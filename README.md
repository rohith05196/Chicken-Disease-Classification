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

## 📸 Sample Images

Healthy vs Coccidiosis-infected chicken fecal samples:

| Healthy | Coccidiosis |
|--------|-------------|
| ![](https://i.imgur.com/xpUdfdx.jpg) | ![](https://i.imgur.com/7elPH5B.jpg) |

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

### 4. Run the Application

```bash
python app.py
```

Navigate to `http://localhost:5000` to use the web app.

---

## 📦 Docker Deployment

To build and run using Docker:

```bash
docker build -t chicken-disease-app .
docker run -p 5000:5000 chicken-disease-app
```

---

## 📊 Model Pipeline Overview

1. **Data Ingestion**  
   Downloads and extracts raw image data.

2. **Data Validation**  
   Verifies format, structure, and integrity of dataset.

3. **Model Training**  
   Fine-tunes a pre-trained CNN using TensorFlow and saves the model.

4. **Model Evaluation**  
   Validates model using test data and logs metrics.

5. **Prediction Pipeline**  
   Accepts new image inputs and returns real-time predictions via the Flask interface.

---

## 🧪 Technologies Used

- Python 3.8
- TensorFlow / Keras
- Flask
- DVC (Data Version Control)
- GitHub Actions
- Docker
- Heroku / AWS / GCP for optional deployment
