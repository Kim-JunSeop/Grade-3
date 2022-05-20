import cv2
from Common.utils import print_matInFo

#gray 영상 파일 읽기
title1,title2 = "gray2gray", "grea2color" #윈도우 이름
gray2gray = cv2.imread("images/read_gray.jpg", cv2.IMREAD_GRAYSCALE) #영상 파일 적재
gray2color = cv2.imread("images/read_gray.jpg",cv2.IMREAD_COLOR)
if gray2gray is None or gray2color is None : #예외처리 - 영상 파일 읽기 여부 조사
    raise  Exception("영상파일 읽기 에러")

#행렬 내 한 화소 값 표시
print("행렬 좌표 (100,100) 화소값")
print("%s %s" % (title1,gray2gray[100,100]))
print("%s %s\n" %(title1, gray2gray [100,100]))

print_matInFo(title1,gray2gray)
print_matInFo(title2,gray2color)

cv2.imshow(title1, gray2gray)
cv2.imshow(title2,gray2color)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("\n")
# color 영상 파일 읽기
title1, title2 = "color2gray","color2color"
color2gray = cv2.imread("images/read_color.jpg",cv2.IMREAD_GRAYSCALE)
color2color = cv2.imread("images/read_color.jpg",cv2.IMREAD_COLOR)
if color2gray is None or color2color is None:
    raise Exception("영상 파일 읽기 에러")

print("행렬 좌표 (100,100) 화소값")
print("%s %s" % (title1,color2gray[100,100])) #한 화소값 표시
print("%s %s\n" % (title1,color2color[100,100]))

print_matInFo(title1,color2gray)  #행렬 정보 출력
print_matInFo(title2,color2color)

cv2.imshow(title1,color2gray)                        #행렬 정보 영상으로 띄우기
cv2.imshow(title2,color2color)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("\n")

#16비트 & 32비트 영상 파일 읽기
title1, title2 = "16bit unchanged", "32bit unchanged" #윈도우 이름
color2unchanged1 = cv2.imread("images/read_16.tif",cv2.IMREAD_UNCHANGED)
color2unchanged2 = cv2.imread("images/read_32.tif",cv2.IMREAD_UNCHANGED)
if color2unchanged1 is None or color2unchanged2 is None:
    raise Exception("영상파일 읽기 에러")

print("16비트/32비트 영상 행렬 좌표 (10,10) 화소값")
print(title1, " 원소 자료형", type(color2unchanged1[10][10][0])) #원소 자료형
print(title1,"화소값(3원소)", color2unchanged1[10,10])           #행렬 내 한 화소 값 표시
print(title2,"원소 자료형", type(color2unchanged2[10][10][0]))
print(title2,"화소값(3원소)", color2unchanged2[10,10])
print()

print_matInFo(title1,color2unchanged1)
print_matInFo(title2,color2unchanged2)

cv2.imshow(title1,color2unchanged1)
cv2.imshow(title2,(color2unchanged2*255).astype("uint8"))

cv2.waitKey(0)