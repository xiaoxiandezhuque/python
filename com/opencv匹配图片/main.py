# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv2.imread('22222.png',0)
# img2 = img.copy()
# template = cv2.imread('yellow.png',0)
# w, h = template.shape[::-1]
#
# # All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
#
# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)
#
#     # Apply template Matching
#     res = cv2.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#
#     cv2.rectangle(img,top_left, bottom_right, 255, 2)
#
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#
#     plt.show()

import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import time
import datetime

def cleanSet(pointSet, newSet):
    if pointSet:
        point = pointSet.pop()
        newSet.add(point)
        removeSet = set()
        for p in pointSet:
            if abs(point[0] - p[0]) <= 3 and abs(point[1] - p[1]) <= 3:
                removeSet.add(p)
    else:
        return
    pointSet -= removeSet
    cleanSet(pointSet, newSet)

t = time.time()
nowTime = int(round(t * 1000))
print (nowTime);

img_rgb = cv2.imread('4.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('other1.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
count = 0
pointSet = set()
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + int(w/2), pt[1] + int(h/2)), (0, 0, 255), 2)
    count += 1
    pointSet.add(pt)
    # print(pt)

newSet = set()
# print(pointSet)
cleanSet(pointSet, newSet)
# print(count)

print(newSet)
print(len(newSet))

t = time.time()
nowTime1 = int(round(t * 1000))
print (nowTime1-nowTime);

cv2.imwrite('111111.png', img_rgb)





a =Image.open("111111.png")
a.show()
