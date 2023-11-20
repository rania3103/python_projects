#!/usr/bin/python3
"""resize image"""
import cv2
img = cv2.imread("images/baby.jpg")
new_img = cv2.resize(img, (200, 2000))  # (width, height)
cv2.imshow("rania", new_img)
cv2.waitKey(0)
