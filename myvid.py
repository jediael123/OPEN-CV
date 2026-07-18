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
        img = Image.open(os.path.join(path,i))
        w,h = img.size
        meanheight+=h
        meanwidth+=w
meanwidth = meanwidth//count
meanheight = meanheight//count

for i in os.listdir("."):
    if i.endswith(".png") or i.endswith(".jpg"):
        img = Image.open(os.path.join(path,i))
        img = img.resize((meanwidth,meanheight),Image.Resampling.LANCZOS)
        img.save(i,"JPEG",quality=95)
