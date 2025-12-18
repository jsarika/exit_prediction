import streamlit as st
st.title("my first streamlit app")
name=st.text_input("enter your name")
st.write("hello",name)
age=st.slider("age",0,100)
st.write("your age is",age)
 
if st.button("say hello"):
 st.write(f"hello {name},nice to meet you")

gender=st.radio("Select Gender",["Male","female","other"])
st.write("You selected:", gender)

feedback = st.text_area("Enter your feedback")
st.write("You wrote:", feedback)

height = st.number_input("Enter your height in cm", min_value=50, max_value=250)
st.write("Your height:", height)

color = st.selectbox("Pick a color", ["Red", "Green", "Blue"])
if color == "Red":
    st.write("Stop! Danger ahead!")
else:
    st.write(f"You picked {color}.")
    
