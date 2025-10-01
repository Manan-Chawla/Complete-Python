import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mini Dashboard for Electronic Shop ")

file=st.file_uploader("Upload your csv file here : ",type=["csv"])

if file:
    df=pd.read_csv(file)
    
    df["dom"]=pd.to_datetime(df["dom"])
    df["doe"]=pd.to_datetime(df["doe"])
    
    st.success("file upload successfully")
    st.subheader("Data Preview : ")
    st.dataframe(df)
    
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        st.write("Bar chart for the data ")
        fig,ax=plt.subplots()
        ax.bar(df["srno"],df["discount"],color="slateblue")
        plt.ylabel("Srno : ")
        plt.xlabel("Discount : ")
        st.pyplot(fig)
        
    with col2:
        st.write("Line Chart for the data")
        fig, ax = plt.subplots()
        ax.plot(df["srno"],df["discount"],color="slateblue")
        plt.ylabel("Srno : ")
        plt.xlabel("Discount : ")
        st.pyplot(fig)
        
    with col3:
        st.write("Area char for data")
        fig,ax=plt.subplots()
        ax.fill_between(df["price"],df["doe"],color="red")
        ax.plot(df["price"], df["doe"], color="red")
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("price")
        plt.xlabel("doe")
        plt.legend()
        st.pyplot(fig)
