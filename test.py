import pickle
import pandas as pd
import numpy as np
import streamlit as st
import tensorflow as tf

from streamlit_option_menu import option_menu

def preprocess_inp(data):
    data = data.copy()

    data['Vegetable'] = data['Vegetable'].replace({
        'cabage': 1,
        'radish': 2,
        'potato': 3,
        'tomato ': 4,
        'peas': 5,
        'pumkin': 6,
        'cucumber': 7,
        'pointed grourd ': 8,
        'Raddish': 9,
        'Bitter gourd': 10,
        'onion': 11,
        'ginger': 12,
        'garlic': 13,
        'califlower': 14,
        'brinjal': 15,
        'okra': 16,
        'chilly': 17,
    })
    return data

model = pickle.load(open("model.pkl",'rb'))

st.title('Check The Expected Price')

col1,col2 = st.columns(2)
    
with col1:
        Vegetable = st.number_input("For Vegetables Enter The Number: \n Cabage -> 1 , Radish -> 2 , Potato -> 3 , Tomato -> 4 , Peas -> 5 , Pumkin -> 6 , Cucumber -> 7 , Pointed grourd -> 8 , Raddish -> 9 , Bitter gourd -> 10, Onion -> 11, Ginger ->12 , Garlic ->13, CauliFlower-> 14, Brinjal ->15, Chilly ->17")
        
with col1:
        Month = st.number_input("Enter The Number of Month")
        
inp = ''

if st.button("Predict"):
        pred = model.predict([[int(Vegetable),int(0),int(37),
                              int(Month),int(0),int(0)]])
#        pred = model.predict([[int(Vegetable),int(Season),int(Temperature),
#                               int(Month),int(Vegetable_Condition),int(Disaster_in_last_3months)]])
       
        st.write("Predicted Price : " , pred[0][0])

