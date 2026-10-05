import streamlit as st
import pickle
st.set_page_config(page_title='da12-prediction')


st.header("DA-12 predictor")
with open("model.pkl","rb") as file:
    model=pickle.load(file)
    yoe=st.number_input("Enter Year of Experience",min_value=0.0,max_value=10.0,step=0.5,value=2.0)
    if st.button("Predict"):
       prediction=model.predict([[yoe]])
       st.success(prediction)
