import cv2
import numpy as np

image = cv2.imread('H://OpenCVData//experiment five//watershed//2.tif')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_gb = cv2.GaussianBlur(gray,(5,5),2)
gray_gb_cn = cv2.Canny(gray_gb,150,90)
cv2.imshow("image1",image)
cv2.imshow("image2",gray_gb)
cv2.imshow("image3",gray_gb_cn)
cv2.findContours(gray_gb_cn,)
cv2.waitKey(0)
cv2.destroyAllWindows()