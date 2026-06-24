import  streamlit as st
from streamlit import button
from variable import message

st.title("hello")

st.button("click me")

if st.button("click MEEE"):
    st.write("Butoni eshte klikuar")

st.checkbox("check me")


if st.checkbox("cli"):
    st.write("e ke klikuar checkbox")


userInput = st.text_input("Enter a text")

st.write("ju keni shenuar:",userInput)

age = st.number_input("enter your age", min_value=0,max_value=200)

st.write("your age is",age)

message = st.text_area("enter a message")

choice = st.radio("pick one",["barcelona","reali","parisi"])

st.write(choice)


if button("regjistrohu"):
    st.success("tani jeni regjistruar me sukses ne platformen tone")