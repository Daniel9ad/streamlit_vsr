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
from streamlit_webrtc import WebRtcMode, webrtc_streamer

import logging
import os
import av
import numpy as np

import streamlit as st
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

logger = logging.getLogger(__name__)

def get_ice_servers():
    """Use Twilio's TURN server because Streamlit Community Cloud has changed
    its infrastructure and WebRTC connection cannot be established without TURN server now.  # noqa: E501
    We considered Open Relay Project (https://www.metered.ca/tools/openrelay/) too,
    but it is not stable and hardly works as some people reported like https://github.com/aiortc/aiortc/issues/832#issuecomment-1482420656  # noqa: E501
    See https://github.com/whitphx/streamlit-webrtc/issues/1213
    """

    # Ref: https://www.twilio.com/docs/stun-turn/api
    try:
        account_sid = "AC0e5bd9b0050252fee5d586318426381d"
        auth_token = "c09854cff0949b74ccb90eb002c858c8"
    except KeyError:
        logger.warning(
            "Twilio credentials are not set. Fallback to a free STUN server from Google."  # noqa: E501
        )
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    client = Client(account_sid, auth_token)

    try:
        token = client.tokens.create()
    except TwilioRestException as e:
        st.warning(
            f"Error occurred while accessing Twilio API. Fallback to a free STUN server from Google. ({e})"  # noqa: E501
        )
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    return token.ice_servers    

video = []
i = 0

def video_frame_callback(frame):
    i += 1
    image = frame.to_ndarray(format="bgr24")
    st.text(type(image))
    video.append(video)

webrtc_ctx = webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={"iceServers": get_ice_servers()},
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)