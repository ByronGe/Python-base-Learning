import cv2

riceImage = cv2.imread("E://pythonWorkspace//python Data//22.png")
se = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
I = cv2.erode(riceImage,se)
J = cv2.dilate(riceImage,se)
kys = cv2.dilate(I,se)
K=J-I
cv2.imshow("riceImage",riceImage)
cv2.imshow("erode",I)
cv2.imshow("dilate",J)
cv2.imshow("kys",kys)
#cv2.imshow("image3",K)






cv2.waitKey(0)
cv2.destroyAllWindows()