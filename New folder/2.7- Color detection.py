import io
import os
import cv2
import csv
import re
#creating csv
import numpy as np


from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
'''
import Tkinter as tk
from Tkinter import *
#from Tkinter import tkFileDialog
'''
root = Tkinter.Tk()
root.withdraw()
test = tkFileDialog.askopenfilename()
#print (test)
testimage=cv2.imread(test)
#print (testimage)


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/balaji.ma/Desktop/Server_port/My First Project-9773d1b60e64.json"
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    test)

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)



draw_bounding_box=[]
text_boundary={}


response = client.text_detection(image=image)
texts = response.text_annotations

for num,text in enumerate(texts):
    if num==0:
        text_identified=text.description
        print (text_identified)
    #print('\n"{}"'.format(text.description))
    vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])
    draw_bounding_box.append(vertices)
    text_boundary[text_identified]=vertices
print (text_boundary)
print (draw_bounding_box)
for i in draw_bounding_box:
    print (i)
with open('opcsv.csv','w+') as file:
        file.write(str(text_identified))
        #file.write('\n')
        

xy=[]
wh=[]
for sno,i in enumerate(draw_bounding_box):
    if sno != 0 :
        for num,i1 in enumerate(i):
            if  num==0:
                xy=[int(s) for s in re.findall(r'\b\d+\b', i1)]
                x=xy[0]
                y=xy[1]
                #print (x)
                #print (y)
            if num==2:
                wh=[int(s) for s in re.findall(r'\b\d+\b', i1)]
                w=wh[0]
                h=wh[1]
                #print (w)
                #print (h)
        cv2.rectangle(testimage,(x,y),(w,h),(0,255,0),2)
		
#Contour detection 

hsv = cv2.cvtColor(testimage, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

#This is for yellow

lower_yellow = np.array([25,50,50])
upper_yellow = np.array([32,255,255])

yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)



# find contours in the thresholded image
image, contours, hierarchy = cv2.findContours(yellow_mask.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
get_all_xywh_position=[]
xywh=[]
#cnt = contours[0]
width=0
x_pos=0
y_pos=0
height=0
for cnt in contours:
    M = cv2.moments(cnt)
    perimeter = cv2.arcLength(cnt,True)
    x,y,w,h = cv2.boundingRect(cnt)
    if w>width:
        width=w
        x_pos=x
        y_pos=y
        height=h
#print (x_pos,y_pos,width,height)
cv2.rectangle(testimage,(x_pos,y_pos),(width+x_pos,y_pos+height),(0,255,0),2)
cv2.putText(testimage, 'Yellow', (x_pos, y_pos+height), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),2)
#print ('xpos',x_pos)
#print('height',height)

#For blue color detection

blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
image, contours, hierarchy = cv2.findContours(blue_mask.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
get_all_xywh_position=[]
xywh=[]
#cnt = contours[0]
width=0
x_pos=0
y_pos=0
height=0
for cnt in contours:
    M = cv2.moments(cnt)
    perimeter = cv2.arcLength(cnt,True)
    x,y,w,h = cv2.boundingRect(cnt)
    if w>width:
        width=w
        x_pos=x
        y_pos=y
        height=h
#print (x_pos,y_pos,width,height)
cv2.rectangle(testimage,(x_pos,y_pos),(width+x_pos,y_pos+height),(0,255,0),2)
cv2.putText(testimage, 'blue', (x_pos, y_pos+height), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),2)
#print ('xpos',x_pos)
#print('height',height)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image', 600,600)
#cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
#cv2.imshow('image',testimage)

		
#Contour detection 

hsv = cv2.cvtColor(testimage, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

#This is for yellow

lower_yellow = np.array([25,50,50])
upper_yellow = np.array([32,255,255])

yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)



# find contours in the thresholded image
image, contours, hierarchy = cv2.findContours(yellow_mask.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
get_all_xywh_position=[]
xywh=[]
#cnt = contours[0]
width=0
x_pos=0
y_pos=0
height=0
for cnt in contours:
    M = cv2.moments(cnt)
    perimeter = cv2.arcLength(cnt,True)
    x,y,w,h = cv2.boundingRect(cnt)
    if w>width:
        width=w
        x_pos=x
        y_pos=y
        height=h
#print (x_pos,y_pos,width,height)
cv2.rectangle(testimage,(x_pos,y_pos),(width+x_pos,y_pos+height),(0,255,0),2)
cv2.putText(testimage, 'Yellow', (x_pos, y_pos+height), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),2)
#print ('xpos',x_pos)
#print('height',height)

#For blue color detection

blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
image, contours, hierarchy = cv2.findContours(blue_mask.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
get_all_xywh_position=[]
xywh=[]
#cnt = contours[0]
width=0
x_pos=0
y_pos=0
height=0
for cnt in contours:
    M = cv2.moments(cnt)
    perimeter = cv2.arcLength(cnt,True)
    x,y,w,h = cv2.boundingRect(cnt)
    if w>width:
        width=w
        x_pos=x
        y_pos=y
        height=h
#print (x_pos,y_pos,width,height)
cv2.rectangle(testimage,(x_pos,y_pos),(width+x_pos,y_pos+height),(0,255,0),2)
cv2.putText(testimage, 'blue', (x_pos, y_pos+height), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),2)
#print ('xpos',x_pos)
#print('height',height)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
#cv2.resizeWindow('image', 600,600)
#cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.imshow('image',testimage)
cv2.waitKey()

