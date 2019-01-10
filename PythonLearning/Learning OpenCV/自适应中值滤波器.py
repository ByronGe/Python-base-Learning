# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 18:29:44 2017

@author: Administrator
"""

import cv2
import numpy as np

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

minSize = 3
maxSize = 7


# 领域统计
def count_neibor(src, i, j):
    count_black = 0
    count_white = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if src[x][y] < 5:
                count_black += 1
            elif src[x][y] > 250:
                count_white += 1
    return count_black, count_white


def adaptiveProcess(src, row, col, kernelSize, maxSize):
    pixels = list()
    for a in range(-kernelSize // 2 + 1, kernelSize // 2 + 1):
        for b in range(-kernelSize // 2 + 1, kernelSize // 2 + 1):
            pixels += [src[row + a, col + b]]
    pixels = sorted(pixels)
    min_ = pixels[0]
    max_ = pixels[kernelSize * kernelSize - 1]
    med = pixels[kernelSize * kernelSize // 2]
    zxy = src[row, col]
    b, w = count_neibor(src, row, col)

    if zxy > 250 and w >= 3:
        return src[row][col]
    elif zxy < 5 and b >= 3:
        return src[row][col]

    if med > min_ and med < max_:
        if zxy > min_ and zxy < max_:
            return zxy
        else:
            return med
    else:
        kernelSize += 2
        if kernelSize <= maxSize:
            return adaptiveProcess(src, row, col, kernelSize, maxSize);
        else:
            return med


src = cv2.imread("H://OpenCVData//experiment two//3.jpg")

src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# src = cv2.resize(src, (352, 288))
medianBlur = cv2.medianBlur(src, 3)

# src1, contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(src,contours,-1,(0,0,255),3)
img1 = cv2.copyMakeBorder(src, maxSize // 2, maxSize // 2, maxSize // 2, maxSize // 2, cv2.BORDER_REFLECT)
adaptive = np.copy(src)

# for k in xrange(np.shape(img1)[2]):
for j in range(maxSize // 2, np.shape(img1)[0] - maxSize // 2):
    for i in range(maxSize // 2, np.shape(img1)[1] - maxSize // 2):
        adaptive[j - maxSize // 2, i - maxSize // 2] = adaptiveProcess(img1, j, i, minSize, maxSize)

# cv2.drawContours(adaptive,contours,-1,(0,0,0),1)

cv2.imshow('adaptived', adaptive)
cv2.imshow('src', src)
# cv2.imshow('src1', src1)
cv2.imshow('medianBlur', medianBlur)

cv2.waitKey()

cv2.destroyAllWindows()