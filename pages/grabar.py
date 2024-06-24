import streamlit as st 

#html_string = '<iframe src="https://daniel31415-vsr-castellano.hf.space" frameborder="0" width="850" height="450"></iframe>'
html_string = '''<script
	type="module"
	src="https://gradio.s3-us-west-2.amazonaws.com/4.31.4/gradio.js"
></script>

<gradio-app src="https://daniel31415-vsr-castellano.hf.space"></gradio-app>
'''
#st.html(html_string)

st.markdown(html_string, unsafe_allow_html=True)