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

def predict_churn(x1,x2,x3,x4,x5,x6):
    input=np.array([[x1,x2,x3,x4,x5,x6]]).astype(np.float64)
    prediction=model.predict(input)
    pred=prediction[0]
    return pred


if nav == 'Prediction':
    
    st.header('Probability to leave the Job')
    
    val1 = st.slider('Satisfaction Level',0.0, 1.0,0.64)
    val2 = st.text_input("Hours worked")
    ques = st.radio(

    "Did you got Promoted last year",

    ('No','Yes'))

    if ques == 'Yes':
        val3 = 1

    if ques == 'No':
        val3 = 0



    choice = st.selectbox(

    'Select your salary category',

    ('Low','Medium','High'))
        
    
    if choice == 'Low':
        high = 0
        low = 1
        medium = 0
    
    if choice == 'Medium':
        high = 0
        low = 0
        medium = 1 

    if choice == 'High':
        high = 1
        low = 0
        medium = 0





    if st.button("Predict"):
        value = predict_churn(val1,val2,val3,high,low,medium)
        if value == 0:
            st.success('Not Leaving the Firm')
        if value == 1:
            st.success('Leaving the Firm')
    
        
        