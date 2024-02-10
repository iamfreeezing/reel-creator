import requests
import pydub

CHUNK_SIZE = 1024
key = "725027c00f3775d3e9a9ee846369f1db"
import os

def generate_audio(sentence: str, api_key: str = key, voice_type: str = "male") -> str:
    url = ""
    if voice_type == 'female':
        url = "https://api.elevenlabs.io/v1/text-to-speech/AZnzlk1XvdvUeBnXmlld"
    elif voice_type == 'male':
        url = "https://api.elevenlabs.io/v1/text-to-speech/29vD33N1CtxCmqQRPOHJ"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": sentence,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }
    response = requests.post(url, json=data, headers=headers)
    
    with open('temp\\record.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    audio = pydub.AudioSegment.from_mp3('temp\\record.mp3')

    return len(audio)/1000