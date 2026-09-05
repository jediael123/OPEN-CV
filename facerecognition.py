import cv2,os,numpy,sys

#load haarcascade file
fascascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
datasets="pix"
subpart = "jediael"

path=os.path.join(datasets,subpart)
if not os.path.isdir(path):
    os.mkdir(path)
width,height = 130,130
cam=cv2.VideoCapture(0)
while cam.isOpened():
    r,frame = cam.read()







                        