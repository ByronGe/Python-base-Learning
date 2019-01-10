import cv2
import numpy as np

def nothing():
    pass
def func_change(img):
    img2 = np.maximum(img,0)
    img2 = np.minimum(img,255)
    return np.uint8(img2)

rgb = cv2.imread('D:\\matlab\\2.jpg')
median_rgb = cv2.blur(rgb,(5,5))
cv2.namedWindow("image")


cv2.createTrackbar('light', 'image', 0, 200, nothing)
cv2.createTrackbar('contrast', 'image', 0, 3, nothing)

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    light = cv2.getTrackbarPos("light", 'image')
    contrast = cv2.getTrackbarPos("contrast", 'image')
    piex_image = median_rgb*contrast+light
    last_img = func_change(piex_image)
    cv2.imshow("image",last_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
