import streamlit as st 

st.header("Sistema de reconocimiento visual del habla VSR")

st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/cargar.py", label="Cargar video", icon="1️⃣")
st.page_link("pages/real_time.py", label="Grabar video", icon="2️⃣", disabled=True)