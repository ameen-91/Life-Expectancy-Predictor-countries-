import streamlit as st
import pickle as pk
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

model = pk.load(open(r"abc.pickle", "rb"))

st.title("Life Expectancy Predictor")

Birth_Rate = st.text_input("Birth Rate")
Fertility_Rate = st.text_input("Fertility Rate")
Infant_mortality = st.text_input("Infant mortality")
Maternal_mortality_ratio = st.text_input("Maternal mortality ratio")
Physicians_per_thousand = st.text_input("Physicians per thousand")


k = st.button("Predict")


if k:
    x = pd.DataFrame([[Birth_Rate,Fertility_Rate,Infant_mortality,Maternal_mortality_ratio,Physicians_per_thousand]])
    x.columns = ["Birth Rate","Fertility Rate","Infant mortality","Maternal mortality ratio","Physicians per thousand"]
    prediction = model.predict(x)
    st.markdown(np.round(prediction[0],2))

