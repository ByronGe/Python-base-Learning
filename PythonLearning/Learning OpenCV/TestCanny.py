import cv2
import numpy as np

img = cv2.imread('E://pythonWorkspace//python Data//2.jpg',0)

cv2.imshow('img',img)
img_canny = cv2.Canny(img,50,150)
cv2.Sobel(img,1,-1,0)
cv2.imshow("image",img_canny)

cv2.waitKey(0)
