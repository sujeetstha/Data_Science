import streamlit as st
import pandas as pd

st.title("Transport Analytics Dashboard")

df = pd.read_csv("pipeline_output/predictions.csv")

st.subheader("Prediction Distribution")
st.bar_chart(df['prediction'].value_counts())

st.subheader("Raw Data")
st.dataframe(df.head())
