import cv2,time,numpy as np

cam = cv2.VideoCapture(0)
time.sleep(1)
background = 0
for i in range(60):
    ret,bg = cam.read()
    print(ret,bg)