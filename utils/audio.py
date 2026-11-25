import os
import base64
import requests
from pathlib import Path

from openai import OpenAI

BASE_URL = "https://openrouter.ai/api/v1"

client = OpenAI(
    base_url=BASE_URL,
    api_key=""
)

# # text to audio
# with client.audio.speech.with_streaming_response.create(
#     model="fish-audio/s2.1-pro-free:free",
#     voice="b347db033a6549378b48d00acb0d06cd",
#     input="Hello, how are you?",
#     response_format="mp3"
# ) as response:
#     response.stream_to_file(Path("output.mp3"))

# audio to text
with open("output.mp3", "rb") as f:
    audio_base64 = base64.b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Transcribe this audio."
                },
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": audio_base64,
                        "format": "wav"
                    }
                }
            ]
        }
    ]
)

# print(response.choices[0].message.content)

# # audio to audiowith open("recording.wav", "rb") as f:
#     audio_base64 = base64.b64encode(f.read()).decode("utf-8")

# response = client.chat.completions.create(
#     model="openai/gpt-audio",
#     modalities=["text", "audio"],
#     audio={
#         "voice": "alloy",
#         "format": "wav"
#     },
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_audio",
#                     "input_audio": {
#                         "data": audio_base64,
#                         "format": "wav"
#                     }
#                 }
#             ]
#         }
#     ],
#     stream=True
# )

# audio_chunks = []

# for chunk in response:
#     delta = chunk.choices[0].delta
#     audio = getattr(delta, "audio", None)

#     if audio and audio.get("data"):
#         audio_chunks.append(audio["data"])

# if audio_chunks:
#     Path("response.wav").write_bytes(
#         base64.b64decode("".join(audio_chunks))
#     )