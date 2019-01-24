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
#testimage=cv2.imread(test)
#print (testimage)



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/balaji.ma/Desktop/Server_port/My First Project-9773d1b60e64.json"
# Imports the Google Cloud client library
from google.cloud import vision
#from google.cloud.vision import types

def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision_v1p3beta1 as vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))
localize_objects(test)
