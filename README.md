# Diabetes Prediction System

## Description

The **Diabetes Prediction System** is a comprehensive project aimed at predicting the likelihood of diabetes in patients. The project is divided into three phases:
1. **Phase 1**: Data Preprocessing
2. **Phase 2**: Machine Learning Model Building
3. **Phase 3**: Frontend Development

The system allows users to input patient data through an interactive UI and receive real-time predictions based on trained machine learning models. The backend is built using Python, Pandas, Scikit-learn, TensorFlow, and the frontend is developed using Streamlit.

## Project Structure

```plaintext
Diabetes Prediction System/
│
├── phase1/                # Data Preprocessing
│   ├── data/              # Raw data and processed data
│   ├── notebooks/         # Jupyter notebooks for data preprocessing
│   └── scripts/           # Python scripts for cleaning and merging datasets
│
├── phase2/                # Machine Learning Model Building
│   ├── notebooks/         # Jupyter notebooks for model building and testing
│   ├── models/            # Saved models (Logistic Regression, Random Forest, Neural Networks)
│   └── scripts/           # Python scripts for training models
│
├── phase3/                # Frontend Development
│   ├── app.py             # Streamlit frontend application
│   ├── requirements.txt   # Python dependencies for the frontend
│   └── assets/            # Additional resources like images, CSS for styling
│
└── README.md              # Project documentation
