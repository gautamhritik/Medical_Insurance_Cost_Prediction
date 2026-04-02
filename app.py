import streamlit as st
import numpy as np
import pandas as pd
import pickle

import os

import sklearn
import sys

st.write("Python:", sys.version)
st.write("Sklearn:", sklearn.__version__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_model(file):
    with open(os.path.join(BASE_DIR, file), 'rb') as f:
        return pickle.load(f)

rf = load_model('rf_model.pkl')
rfc = load_model('rfc_model.pkl')
features = load_model('features.pkl')

st.title("Medical Insurance Cost Predictor")

age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
children = st.slider("Children", 0, 5, 0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["northwest", "southeast", "southwest", "northeast"])

sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0

if bmi < 18.5:
    bmi_category = 0
elif bmi < 25:
    bmi_category = 1
elif bmi < 30:
    bmi_category = 2
else:
    bmi_category = 3

smoker_bmi = smoker * bmi

input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'bmi_category': [bmi_category],
    'smoker_bmi': [smoker_bmi],
    'region_northwest': [0],
    'region_southeast': [0],
    'region_southwest': [0]
})

if region == "northwest":
    input_data['region_northwest'] = 1
elif region == "southeast":
    input_data['region_southeast'] = 1
elif region == "southwest":
    input_data['region_southwest'] = 1

input_data = input_data.reindex(columns=features, fill_value=0)

if st.button("Predict"):

    cost = rf.predict(input_data)[0]
    risk = rfc.predict(input_data)[0]

    risk_map = {0: "Low", 1: "Medium", 2: "High"}

    st.subheader("Prediction Results")
    st.write(f"💰 Estimated Cost: ${cost:,.2f}")
    st.write(f"⚠️ Risk Level: {risk_map[risk]}")