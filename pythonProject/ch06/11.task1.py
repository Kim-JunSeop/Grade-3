import cv2
import numpy as np

win_name = 'dst'
trackbar_name1 = 'image1'
trackbar_name2 = 'image2'

img1 = cv2.imread('images/add1.jpg')
img2 = cv2.imread('images/add2.jpg')

def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, alpha, img2, 1-alpha, 0)
    img_con = cv2.hconcat([img1, dst, img2])
    cv2.imshow(win_name, img_con)

def onChange1(y):
    beta = y/100
    dst1 = cv2.addWeighted(img2, beta, img1, 1-beta, 0)
    img_con1 = cv2.hconcat([img1, dst1, img2])
    cv2.imshow(win_name, img_con1)


img_con2 = cv2.hconcat([img1, img1, img2])
cv2.imshow(win_name, img_con2)
cv2.createTrackbar(trackbar_name1, win_name, 0, 100, onChange)
cv2.createTrackbar(trackbar_name2, win_name, 0, 100, onChange1)
cv2.waitKey()
cv2.destroyAllWindows()