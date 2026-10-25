import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('model.sav')

st.title('Sales Prediction App')
st.write('Enter your advertising budget across different media channels to predict sales volume.')

# User inputs
tv = st.number_input('TV Advertising Budget ($)', min_value=0.0, value=100.0, step=1.0)
radio = st.number_input('Radio Advertising Budget ($)', min_value=0.0, value=20.0, step=1.0)
newspaper = st.number_input('Newspaper Advertising Budget ($)', min_value=0.0, value=10.0, step=1.0)

# Predict button
if st.button('Predict Sales'):
    # Structure input data as a DataFrame to keep feature names
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Sales Volume: {prediction:.2f} units')