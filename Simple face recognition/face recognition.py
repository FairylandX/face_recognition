import cv2
import numpy as np
img = cv2.imread('1.jpg')
d = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f = cv2.CascadeClassifier(cv2.haarcascades+'haarcascade_frontalface_default.xml')
a = f.detectMultiScale(d,1.5,2)
for(x,y,w,h) in a:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
cv2.imshow("winname",img)
cv2.waitKey(0)
