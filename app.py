import streamlit as st 
from gradio_client import Client, file
from streamlit_webrtc import webrtc_streamer

# # Cliente huggingface
# client = Client("Daniel31415/VSR-Castellano")

# st.header("Sistema de reconocimiento visual del habla VSR")

# uploaded_file = st.file_uploader("Cargar video", type=['mp4'])
# if uploaded_file is not None:
#     st.video(uploaded_file)
#     # Guardar archivo
#     with open('clip.mp4', "wb") as f:
#         f.write(uploaded_file.read())
#     # Prediccion
#     with st.spinner('Transcribiendo...'):
#         roi, transcript = client.predict(
#         	video_path={"video":file('clip.mp4')},
#         	api_name="/generar_resultados_demo"
#         )
#     st.success(transcript)
#     st.video(roi['video'])
# 
# Camara
# st.header("Grabar")
# webrtc_streamer(
#     key="example"
# )
from streamlit_webrtc import webrtc_streamer
import av


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)