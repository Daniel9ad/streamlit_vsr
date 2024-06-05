import streamlit as st 

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

st.title('Reconocimiento visual del habla')

st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/cargar.py", label="Cargar video", icon="1️⃣")
st.page_link("pages/real_time.py", label="Real time", icon="2️⃣", disabled=True)