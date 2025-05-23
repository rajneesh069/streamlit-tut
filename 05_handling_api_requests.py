import streamlit as st
import requests

st.title("Live currency converter")

inr = st.number_input("Enter the amount in INR", step=0.1)

target_currency = st.selectbox(
    "Choose the currency to convert to:", ["USD", "EUR", "JPY"]
)

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data.get("rates", {}).get(target_currency, 0)
        if rate != 0:
            converted_value: float = float(rate * inr)
            st.success(f"{inr} INR = {converted_value:.2f} {target_currency}")
        else:
            st.error("Currency not found in API response.")
    else:
        st.error("Failed to fetch currency data.")
