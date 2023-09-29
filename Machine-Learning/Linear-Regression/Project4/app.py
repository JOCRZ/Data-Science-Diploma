import streamlit as st
import numpy as np
import pandas as pd
import pickle



model=pickle.load(open('model.pkl','rb'))
data = pd.read_csv('data//carprices.csv')
st.title("Car Price Prediction")
st.image("data//car.jpg", width=600)


nav = st.sidebar.radio("Navigation",["Aim","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)
    st.text('1) Predict price of a mercedes benz that is 4 yr old with mileage 45000')
    if st.button('Ans-1'):
        st.write('33337.0')
    st.text('2) Predict price of a BMW X5 that is 7 yr old with mileage 86000')
    if st.button('Ans-2'):
        st.write('33337.0')
    st.text('3) Tell me the score (accuracy) of your model.')
    if st.button('Score'):
        st.write('0.8719970367825953')

    
    if st.checkbox("Show Table"):
        st.table(data)

def predict_forest(experience,testscore,interviewscore):
    input=np.array([[experience,testscore,interviewscore]]).astype(np.float64)
    prediction=model.predict(input)
    pred= np.round(prediction[0])
    return float(pred)

if nav == 'Prediction':
    
    st.header('Know Your Car Price')
    choice = st.selectbox(

    'Select the Car Model?',

    ('BMW X5','Audi A5','Mercedez Benz C class'))
    if choice == 'BMW X5':
        experience = '0'
    if choice == 'Audi A5':
        experience = '1'
    if choice == 'Mercedez Benz C class':
        experience = '2'
    testscore = st.text_input("Miles")
    interviewscore = st.text_input("Age")



    if st.button("Predict"):
        output=predict_forest(experience,testscore,interviewscore)
        st.success('Your Predicted Car Price is  {}'.format(output))