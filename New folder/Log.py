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
print (test)
testimage=cv2.imread(test)
print (testimage)



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/balaji.ma/Desktop/Server_port/My First Project-9773d1b60e64.json"
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
#from google.cloud import vision_v1p3beta1 as vision
# Instantiates a client
client = vision.ImageAnnotatorClient()
#testimage=cv2.imread('C:/Users/balaji.ma/Desktop/Server port images/1.JPG')
# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    test)

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
#response = client.label_detection(image=image)
#labels = response.label_annotations

#print (labels)
#print('Labels:')
#for label in labels:
    #print(label.description)

draw_bounding_box=[]


response = client.text_detection(image=image)
texts = response.text_annotations
#print('Texts:')
#print (texts)
#text_identified=texts.description
#print (text_identified)
for num,text in enumerate(texts):
    if num==0:
        text_identified=text.description
        print (text_identified)
    #print('\n"{}"'.format(text.description))
    vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])
    draw_bounding_box.append(vertices)
#print draw_bounding_box
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

#cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow('image',testimage)
cv2.waitKey()
