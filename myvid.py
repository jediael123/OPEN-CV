import cv2
import os
from PIL import Image

path = "C:/Users/Dell/Documents/JetLearn/opencv"
os.chdir(path)
meanheight = 0
meanwidth,meanheight = 0,0
print(len(os.listdir(".")))
count = 0
for i in os.listdir("."):
    if i.endswith(".png") or i.endswith(".jpg"):
        count+=1
        print(i)
        img = Image.open(i)
        w,h = img.size
        meanheight+=h
        meanwidth+=w
meanwidth = meanwidth//count
meanheight = meanheight//count

for i in os.listdir("."):
    if i.endswith(".png") or i.endswith(".jpg"):
        img = Image.open(i)
        img = img.resize((meanwidth,meanheight),Image.Resampling.LANCZOS)
        img.save(i,"PNG",quality=95)

def videoGenerator():
    videoname = "myvideo.avi"
    images = []
    for i in os.listdir("."):
        if i.endswith(".png") or i.endswith(".jpg"):
            images.append(i)
    video = cv2.VideoWriter(videoname,0,1,(meanwidth,meanheight))
    for i in images:
        video.write(cv2.imread(os.path.join(".",i)))
    cv2.destroyAllWindows()
    video.release()
videoGenerator()
        