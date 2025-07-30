import pickle
import streamlit as st
model1=pickle.load(open("AreaPrice.pkl","rb"))

def mydeploy():
    st.title("Area Price Prediction")
    area=st.number_input("Enter Your Area")
    pred=st.button("Predict Price")
    if pred:
        x=model1.predict([[area]])
        st.write("The Price of Area:",round(x[0],4))
    
mydeploy()    