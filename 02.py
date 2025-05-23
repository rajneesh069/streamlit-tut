import streamlit as st
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from openai import OpenAI
import datetime


class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(...)

    model_config = SettingsConfigDict(env_file=f".env", extra="ignore")


Config = Settings()

client = OpenAI(
    api_key=Config.OPENAI_API_KEY,
)


def get_quirky_personality(prompt):
    response = client.responses.create(
        input=prompt,
        model="gpt-4o",
        temperature=0.8,
    )
    return response.output_text.strip()


st.title("A fun form!")


name = st.text_input("Please enter your name:")

dob = st.date_input(
    "Please select your date of birth:",
    format="DD/MM/YYYY",
    min_value=datetime.date(day=1, month=1, year=1990),
)

st.write("Please select your height:")

height_feet = st.slider("Feet:", 0, 7, 5, step=1)

height_inches = st.slider("Inches: ", 0, 11, 1, step=1)

weight = st.number_input(
    "Please enter your weight (in kgs): ", min_value=40, max_value=150
)

singer = st.text_input("Who's your favourite singer?")
song = st.text_input("Enter your favourite song:")

hobby = st.text_input("What do you love doing?")

favourite_food = st.selectbox(
    "Among the following which one do you love the most?",
    ["Pasta", "Maggie", "Burger", "Momos", "Soup", "Noodles", "Something else?"],
)

if favourite_food == "Something else?":
    other_fav_food = st.text_input("Then which one's your favourite food?!")

if st.button("Submit"):

    user_profile = f"""
    Name: {name}
    Date of Birth: {dob.strftime('%d/%m/%Y')}
    Height: {height_feet} feet {height_inches} inches
    Weight: {weight} kg
    Favourite Singer: {singer}
    Favourite Song: {song}
    Hobby: {hobby}
    Favourite Food: {other_fav_food if favourite_food == 'Something else?' else favourite_food}"""

    quirky_prompt = (
        "Based on the following details, write a quirky, light-hearted, and fun personality description. "
        "Be creative and entertaining! Here are the details:\n"
        f"{user_profile}"
    )

    with st.spinner("Generating your quirky personality..."):
        description = get_quirky_personality(quirky_prompt)
        st.success("Here's your personality!\n")
        st.markdown(f"### Your Quirky Personality!\n\n{description}")
