import streamlit as st


st.title("Hello World")
st.subheader("Made with streamlit")
st.text("Writing some text using streamlit")
st.write("What does this .write() do?!")


song = st.selectbox(
    "Your fav songs:", ["Hukam by Karan Aujla", "Itz a Hustle", "Admirin' you"]
)


st.write(f"You chose: {song.strip()}")
