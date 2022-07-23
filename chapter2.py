import cv2
import numpy as np


img = cv2.imread("Resources/download.jfif")
kernel = np.ones((5,5),np.uint8)

cv2.imshow("output",img)
imggrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggrey,(7,7),0)
imgcanny = cv2.Canny(img,100,100)
imgdialation =  cv2.dilate(imgcanny,kernel,iterations=1)
imgeroded = cv2.erode(imgdialation,kernel,iterations=1)

cv2.imshow("image",imggrey)
cv2.imshow("blur image",imgblur)
cv2.imshow("canny img",imgcanny)
cv2.imshow("dilation img",imgdialation)
cv2.imshow("eroded img",imgeroded)
cv2.waitKey(0)