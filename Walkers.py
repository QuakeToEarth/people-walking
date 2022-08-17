import cv2
import os
bodyClassfier = cv2.CascadeClassifier('haarcascade_fullbody.xml')
video = cv2.VideoCapture('walking.avi')
while True:
    ret,frame = video.read()
    grayScale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies = bodyClassfier.detectMultiScale(grayScale,1.2,3)
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(74, 255, 98),2)
        cv2.imshow('pedastrian walkin', frame)
    if cv2.waitKey(1) == 32:
        break


video.release()
cv2.destroyAllWindows()