import cv2
import numpy as np
import matplotlib.pyplot as plt
srcimage = cv2.imread('E://pythonWorkspace//python Data//equalizeHistImage.jpg')
r,g,b=cv2.split(srcimage)
# cv2.imshow("srcimage",srcimage)
# cv2.imshow("redSrcImage",r)
# cv2.imshow("greenSrcImage",g)
# cv2.imshow("blueSrcImage",b)

srcimagered = cv2.equalizeHist(r)
srcimagegreen = cv2.equalizeHist(g)
srcimageblue = cv2.equalizeHist(b)
imageMerge = cv2.merge((srcimagered,srcimagegreen,srcimageblue))
cv2.imshow("imageMerge",imageMerge)
# cv2.imwrite("H:\\OpenCVData\\experiment one\\equalizeHistImage.jpg",imageMerge)

kernel = np.array([

    [0,-1,0],
    [-1,5,-1],
    [-1,0,-1]
])
filter2DImage = cv2.filter2D(srcimage,-1,kernel)#-1是通道
cv2.imshow("filter2DImage",filter2DImage)

#伽马矫正1
def gamma_trains(img,gamma):
    gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
    return cv2.LUT(img,gamma_table)
#伽马矫正2
#image2 = np.power(srcimage / 255.0, 2.2)
#cv2.imshow("image2", image2)

image = gamma_trains(srcimage,2.2)
cv2.imshow("image", image)


cv2.waitKey(0)
cv2.destroyAllWindows()