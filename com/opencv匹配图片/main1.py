import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import time
import datetime


img = cv2.imread("image.png")
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(grey, cv2.CV_32F, 1, 0)
# find minimum and maximum intensities
minVal = np.amin(sobelx)
maxVal = np.amax(sobelx)
draw = cv2.convertScaleAbs(sobelx, alpha=255.0/(maxVal - minVal), beta=-minVal * 255.0/(maxVal - minVal))
cv2.namedWindow('image',cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',img)
cv2.waitKey()