import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

num=0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Display the resulting frame
    cv.imshow('frame', frame)
    a = cv.waitKey(1)
    if a == ord('q'):
        break
    if a == ord('s'):
        cv.imwrite(str(num)+".png", frame)
        print(num)
        num+=1
# When everything done, release the capture
cap.release()