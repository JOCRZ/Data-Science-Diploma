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

    target = st.number_input('Target Score')

    col3,col4,col5 = st.columns(3)
    with col3:
        cscore = int(st.number_input('Current Score', step=1))

    with col4:
        overs = int(st.number_input('Overs Completed', step=1))
    
    with col5:
        wickets = int(st.number_input('Wickets Fallen', step=1))


    if cscore > target:
        st.write(team1," Won the Match")
    
    elif cscore == target-1 and overs==20:
        st.write("Match Ended in a Draw")
    
    elif wickets==10 and cscore < target-1:
        st.write(team2," Won the Match")

        
    elif wickets==10 and cscore == target-1:
        st.write('Match tied')
        
    elif team1==team2:
        st.write('To proceed, please select different teams because no match can be played between the same teams')



    else:

        if target >= 0 and target <= 300  and overs >= 0 and overs <=20 and wickets <= 10 and wickets>=0 and cscore>= 0:
            
            if st.button("Predict"):
                    
                        
                    # Calculating the number of runs left for the batting team to win
                    runs_left = target - cscore 
                    
                    # Calculating the number of balls left 
                    balls_left = 120-(overs*6)
                    
                    # Calculating the number of wickets left for the batting team
                    wickets = 10-wickets
                    
                    # Calculating the current Run-Rate of the batting team
                    currentrunrate = cscore / overs
                    
                    # Calculating the Required Run-Rate for the batting team to win
                    requiredrunrate = (runs_left*6)/balls_left

                    values = pd.DataFrame({'batting_team':[team1], 'bowling_team':[team2], 'city':[city], 'runs_left':[runs_left], 'balls_left':[balls_left],
                'wickets_left':[wickets], 'total_runs_x':[target], 'cur_run_rate':[currentrunrate], 'req_run_rate':[requiredrunrate]})
                    
                    result = model.predict_proba(values)

                    lossprob = result[0][0]
                    winprob = result[0][1]
                    
                

                    st.header(team1+"- "+str(round(winprob*100))+"%")

                    st.header(team2+"- "+str(round(lossprob*100))+"%")  

                    
        else:
            st.error('There is something wrong with the input, please fill the correct details')
    
    