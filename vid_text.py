# -*- coding: utf-8 -*-
"""vid/text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zX9QBBPp4T1S2vnHG0r3_x4j14jAWsIs
"""

!pip install opencv-python-headless Pillow pydub

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Define the video file path
video_path = "butterfly.mp4"

# Read the video file
cap = cv2.VideoCapture(video_path)

# Define the output video codec and file name
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_video_name = "output_video.avi"

# Define the output video dimensions and FPS
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create a VideoWriter object
out = cv2.VideoWriter(output_video_name, fourcc, fps, (frame_width, frame_height))

# Loop through each frame of the input video, convert it to grayscale, and write it to the output video
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray)
        cv2_imshow(gray)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the input and output video objects and destroy any remaining windows
cap.release()
out.release()
cv2.destroyAllWindows()