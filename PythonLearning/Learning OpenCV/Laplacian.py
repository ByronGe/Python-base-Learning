import cv2
import numpy as np

img = cv2.imread('H://OpenCVData//experiment five//Laplacian//1.jpg')
img_house = cv2.imread('H://OpenCVData//experiment five//Sobel//1.tif')
img2 = cv2.GaussianBlur(img,(3,3),1.5)
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray_house = cv2.cvtColor(img_house,cv2.COLOR_BGR2GRAY)
gray_la = cv2.Laplacian(gray,-1,ksize=3)
gray_x = cv2.Sobel(gray,-1,1,0)

house_x =cv2.Sobel(gray_house,-1,1,0)
house_y =cv2.Sobel(gray_house,-1,0,1)
cv2.imshow("x",house_x)
cv2.imshow("y",house_y)
result = cv2.addWeighted(house_x,0.5,house_y,0.5,0)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()