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
"""

with open('app.py', 'w') as f:
    f.write(app_code.strip())

requirements_code = """
streamlit
joblib
scikit-learn
pandas
"""

with open('requirements.txt', 'w') as f:
    f.write(requirements_code.strip())

print("Successfully updated app.py with robust path resolution and saved requirements.txt!")
