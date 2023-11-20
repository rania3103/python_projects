#!/usr/bin/python3
"""show image information"""
import cv2
img = cv2.imread("images/car.jpg")
pix = img.size
dim = img.shape
cv2.imshow("rania", img)
print("Number of pixels: ", pix)
print("Dimensions: ", dim)
cv2.waitKey(0)
