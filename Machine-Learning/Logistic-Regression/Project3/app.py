import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah']

model=pickle.load(open('model.pkl','rb'))
st.title("IPL Win Prediction")
st.image("data//ipl.png", width=500)


nav = st.sidebar.radio("Navigation",["About Project","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)

    

def predict_churn(x1,x2,x3,x4,x5,x6):
    input=np.array([[x1,x2,x3,x4,x5,x6]]).astype(np.float64)
    prediction=model.predict(input)
    pred=prediction[0]
    return pred


if nav == 'Prediction':
    
    st.header('Probability to win ')
    
    city = st.selectbox(
    'Select the city where match is played',sorted(cities))

    col1, col2 = st.columns(2)
    with col1:
        team1 = st.selectbox(
        'Select the batting team',sorted(teams))
    with col2:
        team2 = st.selectbox(
        'Select the bowling team',sorted(teams))

    Target = st.number_input('Target Score')

    col3,col4,col5 = st.columns(3)
    with col3:
        cscore = int(st.number_input('Score', step=1))

    with col4:
        overs = int(st.number_input('Over', step=1))
    
    with col5:
        wickets = int(st.number_input('Wickets', step=1))

    col6,col7 = st.columns(2)

    with col6:
        crate = int(st.number_input('Current run rate', step=1,format="%.2f"))
    with col7:
        rrate = int(st.number_input('Require run rate', step=1,format="%.2f"))


   





    if st.button("Predict"):
        value = predict_churn(val1,val2,val3,high,low,medium)
        if value == 0:
            st.success('Not Leaving the Firm')
        if value == 1:
            st.success('Leaving the Firm')
    
        
        