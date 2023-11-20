#!/usr/bin/python3
"""print an image of baby face with a rectangle around his face"""
import cv2
img = cv2.imread("images/baby.jpg")
# top-left, bottom-right, color green, thickness
cv2.rectangle(img, (500, 60), (800, 550), (0, 255, 0), 4)
cv2.putText(img, "baby face", (500, 60),
            cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 0))
cv2.imshow("rania", img)
cv2.waitKey(0)
