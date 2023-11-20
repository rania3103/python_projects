#!/usr/bin/python3
"""when we press on q we quit the program and we press on s we save the new image"""
import cv2

img = cv2.imread("images/car.jpg", 0)
cv2.imshow("rania", img)
k = cv2.waitKey(0)

if k == ord("q"):
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("images/gray_car.jpg", img)
    cv2.destroyAllWindows()
