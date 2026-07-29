# AI-Based Intrusion Detection System (IDS)

## Project Overview

This project presents an AI-based Intrusion Detection System designed to identify malicious activities in IoT network traffic using machine learning techniques. The system classifies network traffic into normal or attack categories and provides explainability using SHAP (SHapley Additive Explanations).

The application is implemented using Streamlit, allowing users to interact with the model through a web-based interface.

---

## Features

* Detection of cyber attacks in network traffic
* Manual input for real-time prediction
* CSV file upload for bulk analysis
* Prediction confidence visualization
* Explainable AI integration using SHAP
* Summary of detected normal and malicious traffic

---

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* SHAP
* Joblib

---

## Project Structure

```
├── app.py
├── test.py
├── train_model.ipynb
├── model/
│   ├── ids_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
├── datasets/
│   └── train.csv
    ├── test.csv
    ├── validation.csv
└── README.md
├── requirements.txt
├── .gitignore
├── docs/
    └──I.S Assignment 3 RP Project.pdf
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/your-username/AI-Based-Intrusion-Detection-System.git
cd AI-Based-Intrusion-Detection-System
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Application

```
streamlit run app.py
```

---

## Dataset

This project uses the CICIoT2023 dataset for training and evaluation.

Dataset Link (Google Drive):
[https://drive.google.com/drive/folders/12nkmEUZdjJUiiwqQksPGLLUyWIEnnKsY?usp=sharing]

---

## Model Details

* Model: Random Forest Classifier
* Task: Multi-class classification
* Dataset: CICIoT2023
* Explainability: SHAP (TreeExplainer)

The model predicts traffic categories and provides feature-level explanations.

---

## Google Drive Resources

Due to GitHub size limitations, large files are hosted externally. Upload the following files to Google Drive and add their links below:

* Dataset (train.csv): [Paste link here]
* Trained Model (ids_model.pkl): [Paste link here]
* Scaler (scaler.pkl): [https://drive.google.com/file/d/14X_frI9a_Zksa4GsyPW6uVsu9gn3ZO_T/view?usp=sharing]
* Label Encoder (label_encoder.pkl): [https://drive.google.com/file/d/14X_frI9a_Zksa4GsyPW6uVsu9gn3ZO_T/view?usp=sharing]
* IDS Model (ids_model.pkl): [Paste link here]

---

## Notes

* Large datasets and model files are excluded from the repository
* Download required files from Google Drive before running the project
* Ensure correct folder structure after downloading

---

## Author

Muqaddas Iftikhar
BS Data Science

---

## Acknowledgment

* CICIoT2023 Dataset
* Open-source machine learning libraries

---
