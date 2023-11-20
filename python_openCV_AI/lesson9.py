#!/usr/bin/python3
"""read frames from a video file and display them using OpenCV in gray."""
import cv2
vid = cv2.VideoCapture("videos/orange.mp4")
while True:
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow( "rania", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
