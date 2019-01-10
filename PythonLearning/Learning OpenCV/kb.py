import cv2
import numpy as np
img = cv2.imread("E://pythonWorkspace//python Data//kb.dib")

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(kernel)
# 腐蚀图像
eroded = cv2.erode(img, kernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded Image", eroded);

# 膨胀图像
dilated = cv2.dilate(img, kernel)
# 显示膨胀后的图像
cv2.imshow("Dilated Image", dilated);
# 原图像
cv2.imshow("Origin", img)

# NumPy定义的结构元素
NpKernel = np.uint8(np.ones((3, 3)))
print(NpKernel)
Nperoded = cv2.erode(img, NpKernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded by NumPy kernel", Nperoded);





# 闭运算
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 显示腐蚀后的图像
cv2.imshow("Close", closed);

# 开运算
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 显示腐蚀后的图像
cv2.imshow("Open", opened)





cv2.waitKey(0)
cv2.destroyAllWindows()