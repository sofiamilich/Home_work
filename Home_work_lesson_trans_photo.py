
# Отзеркалить картинку


# Черно-белое видео для быстрой обработки;


import cv2
import numpy as np

cap = cv2.VideoCapture('video/4k-relaxing-nature-sounds-short-video-clips-of-nature_(videomega.ru).mp4')

while True:
    success, img = cap.read()

    # img = cv2.resize(img,(img.shape[1] // 2, img.shape[0] // 2))
    img = cv2.GaussianBlur(img, (9, 9), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, 100, 100)

    kernel = np.ones((5, 5), np.uint8)

    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imshow('Name', img)
    # cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




# Считать данные с видео:
# cap = cv2.VideoCapture'video/4k-relaxing-nature-sounds-short-video-clips-of-nature_(videomega.ru).mp4'
# Считать данные с веб камеры компа:
cap = cv2.VideoCapture(0)
# Укажем размеры изображения, id  и размер (ширина и высота):
cap.set(3,500)
cap.set(3,600)



# Для работы с меньшим весом и ускорения, нужно: уменьшить точность, увеличить обводку,
# чтобы покрыть все углы, затем уменьшить количество точек:

# вывести в терминал размер картинки:
print(img.shape)

# Изменить размер картинки ( в кортеж передаем новый размер):
new_img = cv2.resize(img,(200,500))

# Уменьшить пропорционально картинку, иуказав в размере индекс ширины 1 и индекс высоты 0:
new_img = cv2.resize(img, img.shape[1]//2,img.shape[0]//2)

# Обрезать часть каотинки, исчисление пикселей от лев верх угла:
cv2.imshow('Res',  img[0:100, 0:150])
# Добавить размытие, указываем степень размытия и умножитель:
img = cv2.GaussianBlur(img,(3,3),0)
# Переведем цветную в серую:
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Найдем угол, укажем точность - вывод в БИНАРНЫЙ формат:
img = cv2.Canny(img, 90, 90)

# Утолщим обводку:
img = cv2.dilate(img, kernel, interations = 1)
# Сначала создадим матрицу:
import numpy as np
kernel = np.ones((5,5), np.uint8)


# Уменьшим жирность линий (формат БИНАРНВЙ быстрый):
img = cv2.erode(img, kernel, iteration = 1)



#
# Трансформация видео с нейросетями:
# ОТЗЕРКАЛИВАНИЕ

img = cv2.imread('Папка/фото.jpg')
img = cv2.flip(img,1)

cv2.imshow('name', img)
cv2.waitKey(0)

# ВРАЩЕНИЕ КАРТИНКИ

def rotate(img_param, angle):
    height, width = img_param.shape[:2]
    point = (width//2, height//2)
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (height, width))

img = rotate(img, 90)
cv2.imshow('name', img)
cv2.waitKey(0)


# СМЕСТИТЬ ИЗОБРАЖЕНИЕ:
def tranform(img_param, x, y):
    mat = np.float32([[1,0,x], [0,1,y]])
    return cv2.warpAffine(img_param, mat,(img_param.shape[1], img_param.shape[0]))
# вызовем функцию и передадим значения х и у:
img = tranform(img, 30, 200)

#
# КОНТУРЫ ИЗОБРАЖЕНИЯ:
img = cv2.imread('Папка/фото.jpg')
# приведем к серому формату:
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Размоем для сглаживания углов:
img = cv2.GaussianBlur(img,(3,3),0)
# Найдем края, чтобы потом найти контур:
img = cv2.Canny(img, 90, 90)

# ИТОГ: ЧЕРНо-БЕЛОЕ ФОТО

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(con)
cv2.imshow('name', img)
cv2.waitKey(0)


# СОЗДАДИМ НОВУЮ КАРТИНКУ ЗА СЧЕТ КОНТУРОВ

img = cv2.imread('Папка/фото.jpg')
new_img = np.zeros(img.shape, dtype = 'uint8')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img,(5,5),0)
img = cv2.Canny(img, 100, 140)
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)


cv2.drawContours(new_img, con, -1, (230, 111, 148), 1)
cv2.imshow('name', new_img)
cv2.waitKey(0)









