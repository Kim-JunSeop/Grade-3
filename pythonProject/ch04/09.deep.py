import numpy as np
import cv2

image = np.full((300,700,3),(255,255,255),np.uint8)
size = (100,50)
orange = (0,165,255)
pt1,pt2 = (80,100),(280,200)
pt3,pt4 = (400,100),(600,200)
pt5 = (180,150)
pt6 = (500,150)
def onMouse(event, x, y, flags,param):
    global title,pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0: pt = (x,y)
        else:
            cv2.rectangle(image,pt1,pt2,(255,0,0),2)
            cv2.ellipse(image,pt5,size,0,45,220,orange,2)
            cv2.imshow(title,image)
    if event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0: pt = (x,y)
        else:
            cv2.rectangle(image,pt3,pt4,(255,0,0),2)
            cv2.ellipse(image,pt6,size,180,40,250,orange,2)
            cv2.imshow(title,image)

pt=(-1,-1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title,onMouse)
cv2.waitKey(0)