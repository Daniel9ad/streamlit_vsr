import streamlit as st 
from streamlit_webrtc import WebRtcMode, webrtc_streamer

import logging
import os
import av
import numpy as np
import queue
import cv2

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
    # try:
    #     account_sid = "AC0e5bd9b0050252fee5d586318426381d"
    #     auth_token = "15f5e4274b051528962c7c1d470d76d4"
    #     # account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    #     # auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    # except KeyError:
    #     logger.warning(
    #         "Twilio credentials are not set. Fallback to a free STUN server from Google."  # noqa: E501
    #     )
    #     return [{"urls": ["stun:stun.l.google.com:19302"]}]
    account_sid = "AC0e5bd9b0050252fee5d586318426381d"
    auth_token = "f11293c98abaaf8bae033939c7a979c5"
    client = Client(account_sid, auth_token)

    try:
        token = client.tokens.create()
    except TwilioRestException as e:
        st.warning(
            f"Error occurred while accessing Twilio API. Fallback to a free STUN server from Google. ({e})"  # noqa: E501
        )
        return [{"urls": ["stun:stun.l.google.com:19302"]}]

    return token.ice_servers

# i = 0
# texto = ''
# frames = []

# def infer():
#     # Guardar archivo
#     # Obtener el tamaño del primer fotograma
#     height, width, channels = frames[0].shape
#     # Crear un objeto VideoWriter
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Codec de video
#     fps = 25.0 # Frames por segundo
#     video_writer = cv2.VideoWriter('clip.mp4', fourcc, fps, (width, height))
#     # Escribir cada fotograma en el archivo de video
#     for frame in frames:
#         video_writer.write(frame)
#     # Liberar el objeto VideoWriter
#     video_writer.release()

#     # Prediccion
#     with st.spinner('Transcribiendo...'):
#         roi, transcript = client.predict(
#         	video_path={"video":file('clip.mp4')},
#         	api_name="/generar_resultados_demo"
#         )
#     # st.success(transcript)
#     # st.video(roi['video'])
#     texto = f'{texto} {transcript}'

# def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
#     i+=1
#     frames.append(frame.to_ndarray(format="bgr24"))
#     if i == 150:
#         i = 0
#         infer()
    # i+=1
    # if i==100:
    #     texto = f'{texto} 1 '
    # if i==120:
    #     texto = f'{texto} 1 '


# result_queue: "queue.Queue[List[Detection]]" = queue.Queue()
# result_queue = queue.Queue()
# result_queue.put('hola')
# result_queue.put('Daniel')

# webrtc_ctx = webrtc_streamer(
#     key="object-detection",
#     mode=WebRtcMode.SENDRECV,
#     rtc_configuration={"iceServers": get_ice_servers()},
#     video_frame_callback=video_frame_callback,
#     media_stream_constraints={"video": True, "audio": False},
#     async_processing=True,
# )

# if st.checkbox("transcript", value=True):
#     if webrtc_ctx.state.playing:
#         labels_placeholder = st.empty()
#         # NOTE: The video transformation with object detection and
#         # this loop displaying the result labels are running
#         # in different threads asynchronously.
#         # Then the rendered video frames and the labels displayed here
#         # are not strictly synchronized.
#         while True:
#             #result = result_queue.get()
#             labels_placeholder.text(texto)



def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:] if flip else img

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)