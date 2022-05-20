import numpy as np, cv2

def bilinear_interpolation(image, size):
    height = image.shape[0]
    width = image.shape[1]

    scale_x = width / size[1]
    scale_y = height / size[0]

    dst = np.zeros(size, image.dtype)

    for i in range(size[0]):
        for j in range(size[1]):
            x, y = np.int32(j * scale_x), np.int32(i * scale_y)
            if x >= width - 1:
                x = x - 1
            if y >= height - 1:
                y = y - 1

            A, B, C, D = np.float32(image[y:y+2, x:x+2].flatten())

            alpha, beta = (j*scale_x - x), (i*scale_y - y)
            E = A + alpha * (B - A)
            F = C + alpha * (D - C)
            X = E + beta * (F - E)

            dst[i, j] = np.clip(X, 0, 255)
    return dst

image = cv2.imread('images/interpolation.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

size = (350, 329)


dst1 = bilinear_interpolation(image, size)
image = cv2.resize(image, (329,350))

cv2.imshow("User_bilinear", image)
cv2.imshow("User_bilinear2", dst1)
cv2.waitKey(0)

