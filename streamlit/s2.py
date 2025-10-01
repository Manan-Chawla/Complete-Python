import streamlit as st
import pandas as pd

st.title("Upload file to check data's preview")

file = st.file_uploader("Upload file here : ",type=["csv"])

if file:
    df=pd.read_csv(file)
    st.subheader("Preview Data ")
    st.dataframe(df)

if file:
    st.subheader("Summary stats ")
    st.write(df.describe())
    
if file:
    nm=df["name"].unique()
    selectedname=st.selectbox("Filter by Name : ",nm)
    filtername=df[df["name"]==selectedname]
    st.dataframe(filtername)