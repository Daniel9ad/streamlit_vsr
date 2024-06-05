import streamlit as st 
from gradio_client import Client, file

# Cliente huggingface
client = Client("Daniel31415/VSR-Castellano")

uploaded_file = st.file_uploader("Cargar video", type=['mp4'])
if uploaded_file is not None:
    st.video(uploaded_file)
    # Guardar archivo
    with open('clip.mp4', "wb") as f:
        f.write(uploaded_file.read())
    # Prediccion
    with st.spinner('Transcribiendo...'):
        roi, transcript = client.predict(
        	video_path={"video":file('clip.mp4')},
        	api_name="/generar_resultados_demo"
        )
    st.success(transcript)
    st.video(roi['video'])