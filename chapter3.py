
#resixe
"""
import cv2
import numpy as np

img = cv2.imread("Resources/download.jfif")
print(img.shape) #to find  shape of image
#221-h,228-w,3-bgr
                            #w,h
imgresize= cv2.resize(img,(300,500))

cv2.imshow("output",img)
cv2.imshow("output 1",imgresize)
cv2.waitKey(0)
"""
#cropping

import cv2
import numpy as np

img = cv2.imread("Resources/download.jfif")
print(img.shape) #to find  shape of image
#221-h,228-w,3-bgr
                 #h      ,w
imgcropped=  img[100:221,0:200]

cv2.imshow("output",img)
cv2.imshow("output 2",imgcropped)
cv2.waitKey(0)
