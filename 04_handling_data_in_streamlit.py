import streamlit as st
import pandas as pd

st.markdown("# Bike Sales Dashboard")

file = st.file_uploader("Please upload your CSV file", type=["csv"])


if file:
    st.success("File uploaded successfully! 🎉🎉")
    st.header("File Preview")
    df = pd.read_csv(file)
    st.dataframe(df)

    st.header("Summary")
    st.dataframe(df.describe())
    selected_column = st.selectbox("Select a column to filter", list(df.columns))

    unique_values = df[selected_column].unique()
    selected_value = st.selectbox(
        f"Select a value from '{selected_column}'", unique_values
    )
    st.dataframe(df[df[selected_column] == selected_value])
