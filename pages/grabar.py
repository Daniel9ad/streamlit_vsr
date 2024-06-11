import streamlit as st 

html_string = '<iframe src="https://daniel31415-vsr-castellano.hf.space" frameborder="0" width="850" height="450"></iframe>'
#st.html(html_string)

st.markdown(html_string, unsafe_allow_html=True)