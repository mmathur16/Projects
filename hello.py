import streamlit as st
import pandas as pd

st.title("Data :blue[Analysis]")

df = pd.read_csv("All Data Main Trans (1).csv", low_memory=False)

df["Total_Paid"] = pd.to_numeric(df["Total_Paid"], errors="coerce")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["User Type"] = df["User Type"].astype(str).str.strip()
df["Order Type"] = df["Order Type"].astype(str).str.strip()

action = st.menu_button(
    "Customer Type",
    options=["New Customers", "Returning Customers", "All Customers"]
)

if action == "New Customers":
    filtered_df = df[df["User Type"] == "New"]

elif action == "Returning Customers":
    filtered_df = df[df["User Type"] == "Repeat"]

else:
    filtered_df = df.copy()

st.write(f"Rows after filtering: {len(filtered_df)}")

tsum = filtered_df["Total_Paid"].sum()
order = filtered_df["increment_id"].count()
new = len(filtered_df[filtered_df["Order Type"] == "One-Off"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"£{tsum:,.0f}")
col2.metric("Total Orders", order)
col3.metric("New Orders", new)

monthly_sales = (
    filtered_df.dropna(subset=["Date", "Total_Paid"])
    .groupby(pd.Grouper(key="Date", freq="ME"))["Total_Paid"]
    .sum()
    .reset_index()
)

monthly_sales["Month"] = monthly_sales["Date"].dt.strftime("%b %Y")

st.subheader("Monthly Sales Trend")

st.line_chart(
    monthly_sales,
    x="Month",
    y="Total_Paid"
)

st.subheader("Top Products Sold")

product_qty = (
    filtered_df["Product_Name"]
    .dropna()
    .value_counts()
    .head(10)
)

st.bar_chart(product_qty)
