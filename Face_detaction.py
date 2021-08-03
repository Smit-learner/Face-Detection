import cv2
import numpy as np

face_det = cv2.CascadeClassifier("fc.xml")
cam = cv2.VideoCapture(0)
while True:
    _, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_det.detectMultiScale(gray, 1.1, 4)
    for x, y, w, h in faces:
        cv2.ractangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("img", img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cam.release()
