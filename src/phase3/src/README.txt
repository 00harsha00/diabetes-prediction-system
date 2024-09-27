# Diabetes Prediction App (app.py)

This is a Streamlit application (`app.py`) for predicting the likelihood of diabetes based on user input of health metrics such as age, BMI, glucose level, HbA1c level, and gender. The application provides an interactive interface for users to input their health metrics and view the predicted probability of diabetes.

## Features:
- Predicts the probability of diabetes and type 2 diabetes based on user input.
- Provides feedback on health metrics including BMI, glucose level, and HbA1c level.
- Displays diagnosis (diabetic or not diabetic) based on the predicted probability.

## How to Use:
1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Run the application by executing `streamlit run app.py` or `python -m streamlit run app.py`in your terminal.
3. Use the sliders and radio buttons in the sidebar to input your health metrics.
4. View the probability of diabetes, type 2 diabetes, and diagnosis on the main page.
5. Get feedback on your health metrics below the diagnosis section.

## Files:
- `app.py`: Contains the main code for the Streamlit application.
- `model.pkl`: Pre-trained logistic regression model for diabetes prediction.
- `preprocessor.pkl`: Preprocessor for transforming user input data.

# Diabetes Dataset Exploration (eda.py)

This Python script (`eda.py`) is designed for Exploratory Data Analysis (EDA) of the diabetes dataset. It provides functionality to load the dataset, apply filters, and visualize the data using various plots.

## Features:
- Load and display the diabetes dataset.
- Apply filters based on states, gender, age range, hypertension, heart disease, diabetes, and smoking status.
- Visualize the dataset using histograms, line charts, bar charts, radar charts, scatter plots, pair plots, box plots, and correlation matrices.
- Obtain insights into the distribution of features, relationships between variables, and overall patterns within the dataset.

## How to Use:
1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Run the script by executing `streamlit run app.py` or `python -m streamlit run app.py` in your terminal.
3. Follow the prompts to explore and analyze the diabetes dataset interactively.
4. Use the provided filters to subset the dataset based on specific criteria.
5. View and interact with the visualizations to gain insights into the dataset's characteristics.

## Files:
- `eda.py`: Contains the main code for exploratory data analysis of the diabetes dataset.
- `diabetes_dataset.csv`: The dataset used for analysis.
