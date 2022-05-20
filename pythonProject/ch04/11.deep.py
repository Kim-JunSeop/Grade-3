import numpy as np
import cv2
import math

def onMouse(event, x, y, flags, param):
    global title, pt, pt_prev, dist , center

    if event == cv2.EVENT_MOUSEMOVE:
        if flags == cv2.EVENT_FLAG_LBUTTON:
            if pt[0]>=0:
                if pt_prev[0] > 0:
                    cv2.line(image,pt,pt_prev,(255,255,255),3,cv2.LINE_AA)

                cv2.line(image, pt,(x,y),(0,0,255),1, cv2.LINE_AA)
                pt_prev = (x,y)
                cv2.imshow(title, image)
    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x, y)
        else:
            pt_prev = (x, y)
            cv2.line(image, pt, pt_prev, (0,0,255), 2)
            cv2.imshow(title, image)

    if event == cv2.EVENT_LBUTTONUP:
        cv2.line(image,pt,pt_prev,(255,255,255),3),cv2.LINE_AA

        cv2.rectangle(image, pt, pt_prev, (255, 0, 0))
        center = (pt[0]+(np.abs(pt[0]-pt_prev[0]))//2, pt[1]+(np.abs(pt[1]-pt_prev[1]))//2)
        dist = np.linalg.norm(np.array(pt)-np.array(center))
        dist = int(np.abs(np.round(dist, 1)))
        cv2.ellipse(image, center, (dist, dist), 0, 40, 250, (0, 165, 255), 2)
        cv2.imshow(title, image)
        pt = (-1, -1)
image = np.full((300, 500, 3), (255, 255, 255), np.uint8)
pt = (-1, -1)
pt_prev = (-1, -1)
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)