import streamlit as st
import numpy as np
import joblib


import random

random_factor = random.uniform(0.9, 1.2)


# Load the pre-trained model
model = joblib.load('prediction_model_2.pkl')  # Replace 'your_model_file.pkl' with the path to your model file

# Define the Streamlit app
def main():
    # Set the title of the app
    st.title('Prediction App')

    # Add number input widgets for user to enter input values
    input1 = st.number_input('Enter input I:', value=0)
    input2 = st.number_input('Enter input TON:', value=0)

    # Check if inputs are integers
    if not (isinstance(input1, int) and isinstance(input2, int)):
        st.error('Please enter integer values for input I and input TON.')
        return
    if st.button('Predict'):
    # Make prediction using the model
        prediction = model.predict(np.array([[input1, input2]]))

    # Display the prediction

        st.write('Prediction:', prediction)
        st.write('SR:', 0)
        st.write('WLT:', 1)
        st.write('MRR:', 2)


    # Run the app
if __name__ == '__main__':
    main()