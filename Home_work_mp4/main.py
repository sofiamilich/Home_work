import cv2

# Загрузка каскада Хаара для глаз
eye_cascade = cv2.CascadeClassifier('faces.xml')


# Функция для обработки каждого кадра
def pr_processing(processing):
    # Преобразование картинки в ч/б
    gray = cv2.cvtColor(processing, cv2.COLOR_BGR2GRAY)

    # Нахождение глаз на картинке
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)


    # Размеры для размытия
    for (x, y, w, h) in eyes:
        x_expand = max(x - 10, 0)
        y_expand = max(y - 10, 0)
        w_expand = min(w + 20, processing.shape[1] - x_expand)
        h_expand = min(h + 20, processing.shape[0] - y_expand)

        blurred_eye = cv2.GaussianBlur(processing[y_expand:y_expand + h_expand, x_expand:x_expand + w_expand],
                                       (15, 15), 0)

        # Перевожу в ч/б
        gray_eye = cv2.cvtColor(blurred_eye, cv2.COLOR_BGR2GRAY)

        # Создаю трехканальное чб изображение
        gray_eye_colored = cv2.merge([gray_eye] * 3)

        # Наложение чб области вокруг глаз
        processing[y_expand:y_expand + h_expand, x_expand:x_expand + w_expand] = gray_eye_colored

    return processing


cap = cv2.VideoCapture('video_2024.mp4')

while True:
    ret, processing = cap.read()
    if not ret:
        break

    processed_frame = pr_processing(processing)

    cv2.imshow('Video', processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()










# ЧЕРНОВИК


# import cv2
#
# cap = cv2.VideoCapture('video_2024.mp4')
#
# # faces = cv2.CascadeClassifier('faces.xml')
# while True:
#     succes, img = cap.read()
#     cv2.imshow('Res', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# # grey = cv2.CascadeClassifier('faces.xml')
# # grey = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)