from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
root=Tk()
import time

image = Image.open('Automation.jpg')
photo_image = ImageTk.PhotoImage(image)
l = Label(root, image = photo_image)   
l.place(x=0,y=0,relwidth=1, relheight=1)

'''
img = PhotoImage(file = 'D:/Python/Selenium/Working code/titleimage.gif')
root.tk.call('wm', 'iconphoto', root._w, img)
'''
