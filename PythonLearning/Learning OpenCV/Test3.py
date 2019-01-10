import cv2
import numpy as np

img = cv2.imread("E://pythonWorkspace//python Data//4.jpg",0)

element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
img1 = cv2.erode(img,element)
img2 = cv2.dilate(img,element)
img3 = img2 - img1
cv2.imshow("imgee",img3)
ss,result = cv2.threshold(img3,40,255,cv2.THRESH_BINARY)
cv2.imshow("sdf",result)
result = cv2.bitwise_not(result)

cv2.imshow("img3",result)
cv2.waitKey(0)