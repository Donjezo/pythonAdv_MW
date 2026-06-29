import streamlit as st

st.sidebar.header("Sidebar")
st.sidebar.write("this is inside sidebar")

st.sidebar.selectbox("chose an option" ,["Option 1","Option 2","option 3"])

st.sidebar.radio("Go to",["Home","Data","Settings"])