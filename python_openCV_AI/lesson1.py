#!/usr/bin/python3
"""print pixel values in the form of (Blue, Green, Red)"""
import cv2
img = cv2.imread("images/car.jpg")  # read image(pixels of image)
print(img)
