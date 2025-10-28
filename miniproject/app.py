import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mini Dashboard for Electronic Shop")

# Upload file 
file = st.file_uploader("Upload CSV file here:", type=["csv"])

if file:
    # Read CSV
    df = pd.read_csv(file)

    # Convert date columns to datetime
    df["dom"] = pd.to_datetime(df["dom"])
    df["doe"] = pd.to_datetime(df["doe"])

    st.success("File uploaded successfully")
    st.subheader("Preview of Data")
    st.dataframe(df)

    # Summary statistics
    st.subheader("Summary of Data")
    st.write(df.describe(include="all"))

    # Operation 1 : Filter by Name & Price
    df["name_price"] = df["name"] + " - $" + df["price"].astype(str)
    nm = df["name_price"].unique()
    selecteddata = st.selectbox("Filter by Name & Price", nm)
    name_selected, price_selected = selecteddata.split(" - $")
    price_selected = float(price_selected)
    filterdata = df[(df["name"] == name_selected) & (df["price"] == price_selected)]
    
    st.subheader("Filtered Data")
    st.dataframe(filterdata)

    # ==========================
    # 📊 Graphs
    # ==========================

    st.subheader("Visualizations")

    # Bar chart: Product vs Price
    st.write("### Bar Chart: Product Prices")
    fig, ax = plt.subplots()
    ax.bar(df["name"], df["price"], color="skyblue")
    plt.xticks(rotation=90, ha="left")
    plt.ylabel("Price ($)")
    plt.xlabel("Product Name")
    st.pyplot(fig)

    # Area chart: Price vs Discount
    st.write("### Area Chart: Price vs Discount")
    fig, ax = plt.subplots()
    ax.fill_between(df["name"], df["price"], color="lightgreen", alpha=0.5, label="Price")
    ax.plot(df["name"], df["discount"], color="red", marker="o", label="Discount (%)")
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Values")
    plt.xlabel("Product Name")
    plt.legend()
    st.pyplot(fig)

    # Line chart: Price vs Expiry Date (doe)
    st.write("### Line Chart: Price over Expiry Date")
    fig, ax = plt.subplots()
    ax.plot(df["doe"], df["price"], marker="o", color="purple", linewidth=2)
    plt.ylabel("Price ($)")
    plt.xlabel("Expiry Date (DOE)")
    plt.grid(True)
    st.pyplot(fig)
