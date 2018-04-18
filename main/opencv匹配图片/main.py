# import cv2 as cv
# import numpy as np
# from matplotlib import pyplot as plt
# img_rgb = cv.imread('2222.jpg')
# img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
# template = cv.imread('111.png',0)
# w, h = template.shape[::-1]
# res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
# threshold = 0.8
# loc = np.where( res >= threshold)
# for pt in zip(*loc[::-1]):
#     cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
# cv.imwrite('res.png',img_rgb)



import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('2222.jpg',0)
img2 = img.copy()
template = cv.imread('111.png',0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    print(top_left)
    print(f"w  {w}")
    print(f"h  {h}")
    bottom_right = (top_left[0] + w, top_left[1] + h)
    print(bottom_right)
    cv.rectangle(img,top_left, bottom_right, 255, 2)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# mrW=cv2.imread('2222.jpg',1)
# backIMG=cv2.imread('111.png',1)
# plt.figure(0)
# plt.imshow(backIMG)
# plt.figure(1)
# plt.imshow(mrW)
# (WHeight, WWidth, n)=mrW.shape
# result = cv2.matchTemplate(backIMG, mrW, cv2.TM_CCOEFF)
# (_, _, minimumLocation, maximumLocation) = cv2.minMaxLoc(result)
# topLeft = maximumLocation
# bottomRight = ((topLeft[0] + WWidth), (topLeft[1] + WHeight))
# roi = backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]]
# mask = np.zeros(backIMG.shape, dtype="uint8")
# backIMG = cv2.addWeighted(backIMG, 0.25, mask, 0.75, 0)
# backIMG[topLeft[1]:bottomRight[1], topLeft[0]:bottomRight[0]] = roi
# plt.figure(2)
# plt.imshow(backIMG)
# plt.show()
