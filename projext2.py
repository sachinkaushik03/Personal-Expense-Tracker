import streamlit as st

st.title("🧪 Streamlit Basic Function Test")

# Text Input
name = st.text_input("Enter your name:")
st.write("Hello,", name)

# Number Input
age = st.number_input("Enter your age", min_value=0, max_value=100)
st.write("Your age is:", age)

# Slider
rating = st.slider("Rate this app (1-10)", 1, 10)
st.write("Your rating:", rating)

# Checkbox
agree = st.checkbox("I agree to the terms")
if agree:
    st.success("Thanks for agreeing!")

# Radio buttons
gender = st.radio("Select gender:", ["Male", "Female", "Other"])
st.write("Selected gender:", gender)

# Button
if st.button("Click Me"):
    st.balloons()
    st.success("Button Clicked!")

# Selectbox
city = st.selectbox("Choose a city", ["Jaipur", "Jodhpur", "Delhi"])
st.write("You selected:", city)

# File uploader
file = st.file_uploader("Upload a file")
if file:
    st.write("Uploaded: ", file.name)
