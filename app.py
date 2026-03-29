import streamlit as st
import pickle

st.title("YouTube Video Views Prediction")


likes = st.number_input("Enter Likes")
comments = st.number_input("Enter Comments")
title_length = st.number_input("Enter Title Length")


if st.button("Predict Views"):
    engagement_rate = (likes + comments) / 1000

    
    predicted_views = (likes * 2) + (comments * 3) + (title_length * 10)

    st.success(f"Predicted Views: {int(predicted_views)}")