import streamlit as st
import os

st.write("Current folder:", os.getcwd())
st.write("Files here:", os.listdir())
