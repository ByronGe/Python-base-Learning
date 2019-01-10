import cv2
import numpy as np

img = cv2.imread('E://pythonWorkspace//python Data//2.jpg')
cv2.imshow('img',img)
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(GrayImage,240,255,cv2.THRESH_BINARY)

cv2.imshow("image",thresh1)

cv2.waitKey(0)
