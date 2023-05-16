 import os
import moviepy
import moviepy.editor as mp
import tkinter as tk
from google.cloud import speech
import io   

resultat = ""
vrai_fichier_audio = AudioSegment.from_wav(audio_chemin)

# Lecture du fichier audio pour récupérer le taux d'échantillonnage
file_sample_rate = vrai_fichier_audio.frame_rate

    # initialiser les paramètres de l'API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/charlespelong/projects/my-project-soustitres-3b6a4e1a37ac.json'
client = speech.SpeechClient()

config = speech.RecognitionConfig(
        sample_rate_hertz=file_sample_rate,
        language_code='en-US',
        enable_automatic_punctuation=True,
        enable_word_time_offsets=True,
        audio_channel_count=2
    )

with open(audio_chemin, 'rb') as f2:
    byte_data_wav = f2.read()
audio = speech.RecognitionAudio(content=byte_data_wav)

    # transcrire l'audio en texte
response = client.recognize(config=config, audio=audio)

print(response)
print(response.results)