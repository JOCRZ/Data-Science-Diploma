import streamlit as st
import numpy as np
import pandas as pd
import pickle



model=pickle.load(open('model.pkl','rb'))
data = pd.read_csv('data//data.csv')
st.title("Salary Prediction")
st.image("data//salary.jpg", width=600)


nav = st.sidebar.radio("Navigation",["Aim","Prediction"])      

if nav == 'Aim':
    st.markdown(""" #### Aim of the Project """)
    st.markdown(
        """ The csv file contains hiring statics for a firm such as experience of candidate, his written
test score and personal interview score. Based on these 3 factors, HR will decide the
salary. Given this data, you need to build a machine learning model for HR department
that can help them decide salaries for future candidates. Using this predict salaries for
following candidates, """)
    
    if st.checkbox("Show Table"):
        st.table(data)

def predict_forest(experience,testscore,interviewscore):
    input=np.array([[experience,testscore,interviewscore]]).astype(np.float64)
    prediction=model.predict(input)
    pred='{0:.{1}f}'.format(prediction[0], 2)
    return float(pred)

if nav == 'Prediction':
    
    st.header('Know Your Salary')
    experience = st.text_input("Experience")
    testscore = st.text_input("Test Score")
    interviewscore = st.text_input("Interview Score")



    if st.button("Predict"):
        output=predict_forest(experience,testscore,interviewscore)
        st.success('Your Predicted Salary is  {}'.format(output))