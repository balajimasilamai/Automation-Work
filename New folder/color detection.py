import numpy as np
import cv2

img = cv2.imread('C:/Users/balaji.ma/Desktop/Server_port/Kmeans/python-kmeans-dominant-colors/images/batman.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('images',img)
print (contours[0])
'''
# Python program for Detection of a 
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np 
 
# Webcamera no 0 is used to capture the frames
cap = cv2.imread('C:/Users/balaji.ma/Desktop/Server_port/Kmeans/python-kmeans-dominant-colors/images/batman.png')
#cv2.imshow('images',cap)

hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)

#THis is for blue
#lower_red = np.array([110,50,50])
#upper_red = np.array([130,255,255])

#This is for yellow

lower_blue = np.array([25,50,50])
upper_blue = np.array([32,255,255])
range_color=np.array([21,59,84])

# Here we are defining range of bluecolor in HSV
# This creates a mask of blue coloured 
# objects found in the frame.
mask = cv2.inRange(hsv, range_color, upper_blue)
 
# The bitwise and of the frame and mask is done so 
# that only the blue coloured objects are highlighted 
# and stored in res
res = cv2.bitwise_and(cap,cap, mask= mask)
cv2.imshow('frame',cap)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
'''

"""
import cv2
import numpy as np

cap = cv2.imread('imagetest3.jpg')



# Convert BGR to HSV
hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

#This is for yellow

lower_yellow = np.array([25,50,50])
upper_yellow = np.array([32,255,255])

yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

lower_green = np.array([50, 50, 120])
upper_green = np.array([70, 255, 255]) 
green_mask = cv2.inRange(hsv, lower_green, upper_green) # I have the Green threshold image.



# Threshold the HSV image to get only blue colors
blue_mask = cv2.inRange(hsv,lower_blue , upper_blue)
mask = blue_mask + yellow_mask +green_mask
#mask =  green_mask

blue_points = cv2.findNonZero(blue_mask)

green_points = cv2.findNonZero(green_mask)
yellow_points = cv2.findNonZero(yellow_mask)

print (blue_points)
print (len(blue_points))
a=[]
b=[]

for i in range(0,len(blue_points)):
        for j in blue_points[i]:
            #print (j[0])
            #print (j[1])
            b1= j[0]
            b2= j[1]
            a.append(b1)
            b.append(b2)
print (min(a),' ',max(a))
print (min(b),' ',max(b))
'''        
print ('******************')
print (green_points)
print (len(green_points))
print ('******************')
print (yellow_points)
print (len(yellow_points))
'''
cv2.imshow('bounding box',cap[min(a):,max(b)])
'''
for i in (blue_mask):
    for j in range(0,len(i)):
        if i[j] !=255:
            print (i[j],',',j)
'''
# Bitwise-AND mask and original image
res = cv2.bitwise_and(cap,cap,mask=mask)

cv2.imshow('Oringinal image',cap)
cv2.imshow('mask',mask)
cv2.imshow('result',res)
"""

