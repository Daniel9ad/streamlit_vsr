import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Aquí puedes agregar tu código para procesar los frames de video
        return frame

st.title("Prueba de Webcam con Streamlit-webrtc")

webrtc_ctx = webrtc_streamer(
    key="example",
    video_transformer_factory=VideoTransformer,
    media_stream_constraints={
        "video": True,
        "audio": False
    }
)

if webrtc_ctx.video_transformer:
    st.write("Cámara iniciada correctamente.")
else:
    st.write("Esperando iniciar la cámara...")