import streamlit as st
import numpy as np
import pandas as pd
import pickle



model=pickle.load(open('model.pkl','rb'))
data = pd.read_csv('data//HR_comma_sep.csv').head(5)
st.title("Employee Churn Prediction")
st.image("data//churn.png", width=500)


nav = st.sidebar.radio("Navigation",["Aim","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)

    if st.checkbox("Show Table"):
        st.table(data)

def predict_churn(age):
    input=np.array([[age]]).astype(np.float64)
    prediction=model.predict(input)
    pred=prediction[0]
    return pred


if nav == 'Prediction':
    
    st.header('Probability to leave the Job')
    age = st.text_input("Age")
    s-level = st.slider('Satisfaction Level', 0, 130, 25)
    


    if st.button("Predict"):
        value = predict_churn(age)
        if value == 0:
            st.success('Not Buying Insurance')
        if value == 1:
            st.success('Buying Insurance')
    
        
        