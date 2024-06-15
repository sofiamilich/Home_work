import cv2
import numpy as np

# Строим матрицу:
photo1 = np.zeros((440, 470, 3), dtype='uint8')


# Добавляем градиент:
h, w = photo1.shape[0], photo1.shape[1]
for i in range(h):
    for j in range(w):
        photo1[i, j] = (255 - i // 2, 255 - i // 2, 255 - i // 2)  # Градиентное значение цвета


# Добавляем лого:
cv2.circle(photo1,(photo1.shape[1]//2,photo1.shape[0]//2), 177, (255,255,255), thickness = 5)
cv2.line(photo1, (173,172), (209,172), (0, 0,255), thickness = 5)
cv2.line(photo1, (262,172), (295,172), (0, 0,255), thickness = 5)
cv2.line(photo1, (173,177), (173,235), (255, 0,0), thickness = 5)
cv2.line(photo1, (209,177), (209,235), (255, 0,0), thickness = 5)
cv2.line(photo1, (262,177), (262,235), (255, 0,0), thickness = 5)
cv2.line(photo1, (297,177), (297,235), (255, 0,0), thickness = 5)
cv2.ellipse(photo1,(235,235),(62,62),0,0,180,(0, 255, 0),thickness = 5)
cv2.ellipse(photo1,(235,235),(27,27),0,0,180,(0, 255, 0),thickness = 5)


# Запускаем:
cv2.imshow('Logo', photo1)
cv2.waitKey(0)
# plt.show()