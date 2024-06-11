import streamlit as st 

html_string = '<gradio-app src="https://<space-subdomain>.hf.space"></gradio-app>'

st.markdown(html_string, unsafe_allow_html=True)