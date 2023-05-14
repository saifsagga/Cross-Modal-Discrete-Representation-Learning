# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OKYx659y-0_HtNamvTqX9E7kS8NDrRoU
"""

!pip install moviepy
!pip install SpeechRecognition

import speech_recognition as sr
import moviepy.editor as mp

# Load the video file
video_path = "/content/baby.mp4"
clip = mp.VideoFileClip(video_path)

# Extract the audio from the video
audio_path = "temp_audio.wav"
clip.audio.write_audiofile(audio_path)

# Initialize the recognizer
r = sr.Recognizer()

# Transcribe the audio
with sr.AudioFile(audio_path) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)

print(text)