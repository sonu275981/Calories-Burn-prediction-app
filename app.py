import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("calories.pkl", "rb"))  # here wb means read binary 

from PIL import Image
image = Image.open('templete/burn-burn.jpg')
st.image(image)

st.title('Calories Burn prediction')

with st.form(key='columns_in_form'):
    Gender = st.selectbox('Selected your Transmission', ('Female', 'Male'))
    if (Gender == 'Female'):
        Gender = 0
    else:
        Gender = 1
    col1, col2 = st.columns(2)
    with col1:
        Age = st.number_input('Insert Your Age', min_value=18, max_value=79, value=30)
    with col2:
        Height = st.number_input('Insert Your Height (in C.M)', min_value=123.0, max_value=224.0, value=174.0)

    col3, col4 = st.columns(2)
    with col3:
        Weight = st.number_input('Insert Your Weight (in K.G)', min_value=30.0, max_value=132.0, value=74.0)
    with col4:
        Duration = st.number_input('Insert Your Time Duration (in Min)', min_value=1.0, max_value=60.0, value=15.0)

    col5, col6 = st.columns(2)
    with col5:
        Heart_Rate = st.number_input('Insert Your Heart_Rate (HR/M)', min_value=60.0, max_value=150.0, value=95.0)
    with col6:
        Body_Temp = st.number_input('Insert Your Body_Temp (°C)', min_value=37.1, max_value=42.0, value=40.0)

    submitted = st.form_submit_button('Submit')

value = (model.predict(np.array([[Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]])))

value = round(value[0], 2)

st.header(f"Your total burn colories is {value}")
