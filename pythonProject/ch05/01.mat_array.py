import cv2

image = cv2.imread("images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None : raise Exception("영상파일읽기오류 발생") #예외처리

x_axis = cv2.flip(image,0)          #x축 기준 상하 뒤집기
y_axis = cv2.flip(image,1)          #y축 기준 좌우 뒤집기
xy_axis = cv2.flip(image,-1)
rep_image = cv2.repeat(image,1,2)   #반복 복사
trans_image = cv2.transpose(image)  #행렬 전치
trans_image_trans = cv2.transpose(trans_image)  #전치 행렬 다시 전치

#각 행렬을 영상으로 표시
titles = ['image','x_axis','y_axis', 'xy_axis','rep_image','trans_image','trans_image_trans']

for title in titles:
    cv2.imshow(title,eval(title))
cv2.waitKey(0)

