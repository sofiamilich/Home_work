import cv2
import numpy as np



# # Создадим матрицу копию
img = cv2.imread('Video\color_text.jpg')
new_img = np.zeros(img.shape, dtype = 'uint8')

# # # КОНТУРЫ ИЗОБРАЖЕНИЯ:
# # приведем к серому формату:
img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
# # Размоем для сглаживания углов:
img = cv2.GaussianBlur(img,(1,1),1)
# Найдем края, чтобы потом найти контур:
img = cv2.Canny(img,50, 70)
con, hir = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(con)

contour1 = []
contour2 = []
contour3 = []

for contour in con:
    x, y, w, h = cv2.boundingRect(contour)
    if y < img.shape[0] / 5:
        contour1.append(contour)
    elif y < 2 * img.shape[0] / 5:
        contour2.append(contour)
    else:
        contour3.append(contour)

cv2.drawContours(new_img, contour1, -1, (255, 255, 0), 1)
cv2.drawContours(new_img, contour2, -1, (0, 11, 255), 1)
cv2.drawContours(new_img, contour3, -1, (255, 100, 255), 1)

cv2.imshow('Contours', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


