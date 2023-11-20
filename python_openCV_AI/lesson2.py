#!/usr/bin/python3
"""show image in a window"""
import cv2
img = cv2.imread("images/car.jpg")
cv2.imshow("rania", img)
cv2.waitKey(0)
