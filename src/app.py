import streamlit as st
import joblib
import numpy as np
import os
model_path = os.path.join(os.path.dirname(__file__), "..", "volatility_model.pkl")
model = joblib.load(model_path)

#model = joblib.load("../volatility_model.pkl")

st.title("🚀 Crypto Volatility Predictor")

open_p = st.number_input("Open")
high_p = st.number_input("High")
low_p = st.number_input("Low")
close_p = st.number_input("Close")
volume = st.number_input("Volume")
market_cap = st.number_input("Market Cap")

if st.button("Predict Volatility"):
    features = np.array([[open_p, high_p, low_p, close_p, volume, market_cap]])
    pred = model.predict(features)
    st.success(f"Predicted Volatility: {pred[0]:.6f}")
