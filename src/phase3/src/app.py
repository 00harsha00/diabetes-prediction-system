import streamlit as st
import pandas as pd
import joblib

from PIL import Image
img = Image.open("phase3/src/glucometer.png")
c1, c2, c3 = st.columns(3)

with c1:
    st.write(' ')

with c2:
    st.image(img,width=200)

with c3:
    st.write(' ')

def load_models():
    model = joblib.load('phase3/src/model.pkl')
    preprocessor = joblib.load('phase3/src/preprocessor.pkl')
    return model, preprocessor

model, preprocessor = load_models()

def diabetes_app():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
            padding: 20px;
            font-family: Arial, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .stApp {
            background-color: seagreen;
            color: yellow;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Diabetes Prediction Tool')
    st.sidebar.title('User Input')

    age = st.sidebar.slider('Age', min_value=1, max_value=120, value=30, step=1)
    bmi = st.sidebar.slider('BMI', min_value=10.0, max_value=50.0, value=22.0, step=0.1)
    glucose = st.sidebar.slider('Glucose Level (mg/dL)', min_value=50, max_value=200, value=99, step=1)
    hbA1c = st.sidebar.slider('HbA1c Level (%)', min_value=3.5, max_value=15.0, value=5.5, step=0.1)
    gender = st.sidebar.radio('Gender', ['Female', 'Male'])

    user_input_df = pd.DataFrame({
        'year': [2022],
        'age': [age],
        'bmi': [bmi],
        'hbA1c_level': [hbA1c],
        'blood_glucose_level': [glucose],
        'gender': [gender],
        'location': ['Alabama'],
        'smoking_history': ['former'],
    })

    diabetes_probability = predict_diabetes(user_input_df)
    type_2_diabetes_probability = diabetes_probability * 0.7
    feedback = provide_feedback(bmi, glucose, hbA1c)

    st.subheader('Your Health Metrics:')
    st.markdown(
        f"""
        - **Age**: {age}
        - **BMI**: {bmi} - {feedback['BMI']}
        - **Glucose Level**: {glucose} mg/dL - {feedback['Glucose']}
        - **HbA1c Level**: {hbA1c}% - {feedback['HbA1c']}
        """
    )

    st.subheader('Diabetes Assessment')
    st.markdown(
        f"""
        - **Probability of Diabetes**: {diabetes_probability*100:.2f}%
        - **Probability of Type 2 Diabetes**: {type_2_diabetes_probability*100:.2f}%
        - **Diagnosis**: {'Diabetic' if diabetes_probability > 0.5 else 'Not Diabetic'}
        """
    )

    status_color = "yellow" if diabetes_probability > 0.5 else "#38eb8b"
    st.markdown(
        f"""
        <style>
        .stButton>button {{
            background-color: {status_color} !important;
            color: green !important;
            font-family: Arial, sans-serif;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        .stButton>button:hover {{
            opacity: 0.9;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def predict_diabetes(user_input_df):
    input_transformed = preprocessor.transform(user_input_df)
    prediction_proba = model.predict_proba(input_transformed)
    return prediction_proba[0][1]

def provide_feedback(bmi, glucose, hbA1c):
    feedback = {
        'BMI': "Underweight" if bmi < 18.5 else "Normal weight" if bmi <= 24.9 else "Overweight" if bmi <= 29.9 else "Obese",
        'Glucose': "Low" if glucose < 70 else "Normal" if glucose <= 99 else "High (Prediabetic)" if glucose <= 125 else "Very High (Diabetic)",
        'HbA1c': "Normal" if hbA1c < 5.7 else "Elevated (Prediabetic)" if hbA1c <= 6.4 else "High (Diabetic)"
    }
    return feedback

def main():
    diabetes_app()

if __name__ == "__main__":
    main()

