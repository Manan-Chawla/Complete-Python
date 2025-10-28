import streamlit as st
import pandas as pd

st.title("🏠 My First App")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("Hello! This is normal text.")


name = st.text_input("What's your name?")
age = st.number_input("Enter your age:", min_value=1, max_value=100)
agree = st.checkbox("Do you like Streamlit?")

if agree:
    st.write(f"Cool! {name}, age {age}, likes Streamlit 🎉")


if st.button("Say Hello"):
    st.success("Hello there! 👋")

data = {"Name": ["Manan", "Priya", "Bella"], "Age": [24, 25, 19]}
df = pd.DataFrame(data)

st.write("Here is a table:")
st.table(df)

st.write("Here is a chart:")
st.bar_chart(df["Age"])

st.area_chart(df["Name"])