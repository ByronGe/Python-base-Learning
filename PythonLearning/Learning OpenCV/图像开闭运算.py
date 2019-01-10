import cv2
import numpy as np

img = cv2.imread('H://OpenCVData//experiment four//3.jpg')


def nothing():
    pass
kernel = np.ones((5,5),np.uint8)
cv2.namedWindow("opening")
cv2.namedWindow("closing")
cv2.createTrackbar("opening",'opening',1,10,nothing)
cv2.createTrackbar("closing",'closing',1,10,nothing)



while (1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    iterations_opening = cv2.getTrackbarPos("opening",'opening')
    iterations_closing = cv2.getTrackbarPos("closing",'closing')
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=iterations_opening)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=iterations_closing)


    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)

cv2.waitKey(0)