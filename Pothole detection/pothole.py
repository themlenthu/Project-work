#pothole
import cv2
from cv2 import INTER_CUBIC
import numpy as np

def getcontours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:  
     area=cv2.contourArea(cnt)
     peri=cv2.arcLength(cnt,True)
     if area>=500 and area<1000 and peri>100 and peri<150:
         cv2.drawContours(imgcontour,cnt,-1,[0,0,255],3)
         
        

cap = cv2.VideoCapture('C:\\Users\\Krishna\\Downloads\\bolt_test_pothole.mp4')
cv2.namedWindow('video', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret,image=cap.read()
    #img=cv2.resize(image,(640,480),image,0.5,0.5,interpolation=INTER_CUBIC)
    img = image
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imgGray,(9,9),2.5)
    _,thrsh=cv2.threshold(imgblur,150,255,0)
    imgCanny=cv2.Canny(imgblur,150,150)
    imgcontour=img.copy()
    getcontours(thrsh)
    cv2.imshow('video',imgcontour)
    if cv2.waitKey(1) & 0xFF==ord('q'): # press q for quitting the video
        break
cap.release
cv2.destroyAllWindows