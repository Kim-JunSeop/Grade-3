import numpy as np,cv2

image = cv2.imread('images/ssu.jpg')
logo1 = cv2.imread('images/ssu_logo1.jpg')
logo2 = cv2.imread('images/ssu_logo2.jpg')

if image is None or logo1 is None or logo2 is None \
        : Exception("영상 파일 읽기 오류 발생")

cv2.imshow('logo1 origin', logo1)

logo1[0:87, 220:700] = logo2

masks = cv2.threshold(logo1, 230, 255, cv2.THRESH_BINARY)[1]
masks = cv2.split(masks)

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)

(H,W), (h,w) = image.shape[:2], logo1.shape[:2]
x, y = (W-w)//2,(H-h)//2 - 180
roi = image[y:y+h, x:x+w]

foreground = cv2.bitwise_and(logo1, logo1, mask=bg_pass_mask)
background = cv2.bitwise_and(roi, roi, mask=fg_pass_mask)

dst = cv2.add(background,foreground)
image[y:y+h, x:x+w] = dst

cv2.imshow('logo2 origin', logo2) , cv2.imshow('forground', foreground)
cv2.imshow('background', background) , cv2.imshow('logo1 merged', logo1)
cv2.imshow('dst', dst) , cv2.imshow('image', image)

cv2.waitKey()
