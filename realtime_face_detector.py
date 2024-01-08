import cv2




def detect_bound_box(vid):  #detect and draws rectangle on faces

    img_gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    # settings for detecting faces
    faces = face_classifier.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 20))

    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x,y),(x+w, y+h), (0, 255, 0), 4)

    return faces

# load face identifier
face_classifier = cv2.CascadeClassifier( cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# load camera
video_capture = cv2.VideoCapture(0)



while True :
    # read the frame
    results, video_frame = video_capture.read()

    if results is False:
        break

    face = detect_bound_box(video_frame)

    cv2.imshow('Face detector', video_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()





















