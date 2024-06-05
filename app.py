import streamlit as st 

st.title('Reconocimiento visual del habla')

st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/cargar.py", label="Cargar video", icon="1️⃣")
st.page_link("pages/real_time.py", label="Real time", icon="2️⃣", disabled=True)