import numpy as np
import cv2
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
import time

from tensorflow.keras.models import load_model

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

model = load_model('../models/BaselineM5-weights-best.hdf5')

cap=cv2.VideoCapture(0)

timeList = []
while True:
    ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
    if not ret:
        continue
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)


    for (x,y,w,h) in faces_detected:
        cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),thickness=5)
        roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image
        roi_gray=cv2.resize(roi_gray,(48,48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        img_pixels /= 255

        time1 = time.time()
        predictions = model.predict(img_pixels)
        time2=time.time()
        timeList.append(time2-time1)
        print(time2-time1)

        timeList.append(time2-time1)

        #find max indexed array
        max_index = np.argmax(predictions[0])
        probability = predictions[0][max_index]

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]
        probability = predictions[0][max_index]

        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Facial emotion recognition system ',resized_img)



    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break

print(sum(timeList) / len(timeList))
cap.release()
cv2.destroyAllWindows