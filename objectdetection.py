import cv2
import numpy as np
dino = cv2.imread("car.png",1)
greydino = cv2.cvtColor(dino,cv2.COLOR_BGR2GRAY)
blurdino =cv2.blur(greydino,(3,3))
detectedcircle = cv2.HoughCircles(blurdino,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)
if  detectedcircle is not None:
    detectedcircles = np.uint16(np.around(detectedcircle))
    for i in detectedcircles[0,:]:
        print(i)
        x,y,r = i
        cv2.circle(dino,(x,y),r,(255,0,0),3)
        cv2.circle(dino,(x,y),1,(255,0,0),5)
    cv2.imshow("detectedcircles",dino)
    cv2.waitKey(0)
