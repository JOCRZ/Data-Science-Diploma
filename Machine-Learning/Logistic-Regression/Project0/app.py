import streamlit as st
import numpy as np
import pandas as pd
import pickle



model=pickle.load(open('model.pkl','rb'))
data = pd.read_csv('data//insurance_data.csv')
st.title("Insurance Buy Probability Prediction")
st.image("data//insurance.jpg", width=500)


nav = st.sidebar.radio("Navigation",["Aim","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)

    if st.checkbox("Show Table"):
        st.table(data)

def predict_buy(age):
    input=np.array([[age]]).astype(np.float64)
    prediction=model.predict(input)
    pred=prediction[0]
    return pred


if nav == 'Prediction':
    
    st.header('Probability to Buy Insurance')
    age = st.text_input("Age")
    


    if st.button("Predict"):
        value = predict_buy(age)
        if value == 0:
            st.success('Not Buying Insurance')
        if value == 1:
            st.success('Buying Insurance')
    
        
        