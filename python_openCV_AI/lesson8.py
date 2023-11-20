#!/usr/bin/python3
"""read frames from a video file and display them using OpenCV."""
import cv2
vid = cv2.VideoCapture("videos/orange.mp4")
while True:
    ret, frame = vid.read()
    cv2.imshow( "rania", frame)
    if cv2.waitKey(1) and 0xFF == ord("q"):
        break
