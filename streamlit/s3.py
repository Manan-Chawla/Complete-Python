import streamlit as st
import requests

st.title("💱 Live Currency Converter")

# Input amount in INR
amount = st.number_input("Enter amount in INR:", min_value=1)

# Choose target currency
targetcurrency = st.selectbox("Convert to:", ["USD", "EUR", "GBP", "JPY"])

# Button to trigger conversion
if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        rate = data["rates"].get(targetcurrency)

        if rate:
            converted_amount = amount * rate
            st.success(f"{amount} INR = {converted_amount:.2f} {targetcurrency}")
        else:
            st.error("Currency not available in API response.")
    else:
        st.error("Failed to fetch exchange rates. Try again later.")


# python ---> advanced
# gen ai + langchain
# node js 
# express js
# axion
# api --> soapful or restful api