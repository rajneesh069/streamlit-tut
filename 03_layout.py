import streamlit as st

st.markdown("# Pick your likes!")

col1, col2 = st.columns(2)

if "vote" not in st.session_state:
    st.session_state.vote = None

with col1:
    col1.header("Travelling")
    col1.image(
        "https://images.pexels.com/photos/3278215/pexels-photo-3278215.jpeg?cs=srgb&dl=pexels-freestockpro-3278215.jpg&fm=jpg",
        width=200,
    )
    if st.button("Vote for Travelling!"):
        st.session_state.vote = "travelling"

with col2:
    col2.header("Food")
    col2.image(
        "https://www.archanaskitchen.com/images/archanaskitchen/0-Archanas-Kitchen-Recipes/Articles/momo_noodles_soup_2018.jpg",
        width=200,
    )
    if st.button("Vote for Food!"):
        st.session_state.vote = "food"

if st.session_state.vote == "travelling":
    st.success("You voted for Travelling... You're an adventurer!!")
elif st.session_state.vote == "food":
    st.success("You voted for Food... You're a real foodie!!")

st.sidebar.markdown("# Some Info")
name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.number_input("Enter your age", step=1, min_value=20)

fav_place = ""
fav_food = ""
if st.session_state.vote == "travelling":
    fav_place = st.sidebar.text_input("Which is your favourite place?")
elif st.session_state.vote == "food":
    fav_food = st.sidebar.text_input("Which food is your favourite?")

if fav_food or fav_place:
    st.success(
        f"Awesome! So you like {fav_place if fav_place else fav_food}! Good Choice....🎊"
    )
