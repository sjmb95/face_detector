import cv2
import matplotlib.pyplot as plt
imgPath = 'passport_salim.jpg'

imgPath = input("file name > ")

img = cv2.imread(imgPath)

img.shape

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray.shape

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

face = face_classifier.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

for (x, y, w, h) in face:
    cv2.rectangle(img, (x,y,), (x+w, y+h), (0, 255, 0), 4)


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# cv2.imshow('face detection', img)
# cv2.waitKey()


plt.figure(figsize=(20, 10))
plt.imshow(img_rgb)
plt.axis('off')
plt.show()






















