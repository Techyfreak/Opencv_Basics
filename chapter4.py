import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)
print(img)
#img[200:300,100:300]=500,50,500

#img[:]=500,50,500

#cv2.line(img,(0,0),(400,350),(250,0,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(250,0,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),4)
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,0,0),4)
cv2.putText(img,"Opencv",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow("image",img)

cv2.waitKey(0)