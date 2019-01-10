import numpy as np
import cv2

srcImg = cv2.imread("H://OpenCVData//experiment one//1.jpg")


# cv2.namedWindow('image')
# cv2.imshow ('image', srcImg)


# 1 结合滑动条调整图像亮度和对比度
def set_to_0_255(img):
    img2 = np.maximum(img, 0.0)
    img2 = np.minimum(img, 255.0)
    return np.uint8(img2)


def nothing():
    pass


cv2.namedWindow('Image')
cv2.createTrackbar('light', 'Image', 0, 200, nothing)
cv2.createTrackbar('contrast', 'Image', 100, 300, nothing)
while (1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    light_val = cv2.getTrackbarPos('light', 'Image')
    consrast_val = cv2.getTrackbarPos('contrast', 'Image') / 100.0
    srcImg2 = consrast_val * srcImg + light_val
    srcImg2 = set_to_0_255(srcImg2)
    cv2.imshow("Image", srcImg2)

cv2.destroyAllWindows()
