#!/usr/bin/python3
"""color system in image"""
import cv2
img = cv2.imread("images/baby.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert color TO GRAY
cv2.imshow("rania", gray)
cv2.waitKey(0)