import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Title
st.title("📊 Sales Data Dashboard")

# Load Data
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

st.subheader("🔍 Dataset Preview")
st.dataframe(df)

# KPIs
st.subheader("📌 Key Metrics")

total_sales = df["Sales"].sum()
best_product = df.groupby("Product")["Sales"].sum().idxmax()

st.metric("Total Sales", total_sales)
st.metric("Best Product", best_product)

# Monthly Sales Chart
st.subheader("📈 Monthly Sales")

monthly_sales = df.groupby("Month")["Sales"].sum()

fig, ax = plt.subplots()
monthly_sales.plot(kind="bar", ax=ax)

st.pyplot(fig)

# Filter by Region
st.subheader("🌍 Sales by Region")

region = st.selectbox("Choose Region:", df["Region"].unique())

filtered = df[df["Region"] == region]

st.write(filtered)

st.write("Total Sales in Region:", filtered["Sales"].sum())