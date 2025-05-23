import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

st.header("Age Calculator")

today = datetime.datetime.now()
dob = st.date_input(
    "Enter your date of birth:",
    min_value=datetime.date(day=1, month=1, year=1991),
    format="DD/MM/YYYY",
)

delta = relativedelta(today, dob)
if delta.years != 0:
    st.success(
        f"Your age is: {delta.years} years, {delta.months} months, and {delta.days} days!"
    )
