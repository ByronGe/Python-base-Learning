import cv2

lenaImage = cv2.imread("H://OpenCVData//experiment two//2.jpg")
cv2.imshow("lena",lenaImage)

lena_median = cv2.medianBlur(lenaImage,9)
cv2.imshow("lena_median",lena_median)


rectImage = cv2.imread("H://OpenCVData//experiment two//3.jpg")
#cv2.imshow("lena",rectImage)







cv2.waitKey(0)
cv2.destroyAllWindows()