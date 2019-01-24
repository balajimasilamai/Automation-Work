
import cv2
import numpy as np
import imutils
cap = cv2.imread('imagetest1.jpg')



# Convert BGR to HSV
hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

#This is for yellow

lower_yellow = np.array([25,50,50])
upper_yellow = np.array([32,255,255])

yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# find contours in the thresholded image
image, contours, hierarchy = cv2.findContours(yellow_mask.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print (contours)
#img = cv2.drawContours(cap, contours, -1, (255,0,0), 3)
#cv2.imshow('image',cap)
get_all_xywh_position=[]
xywh=[]
cnt = contours[0]
width=0
x_pos=0
y_pos=0
height=0
#print ((contours))
for cnt in contours:
    M = cv2.moments(cnt)
    perimeter = cv2.arcLength(cnt,True)
    x,y,w,h = cv2.boundingRect(cnt)
    if w>width:
        width=w
        x_pos=x
        y_pos=y
        height=h
        
    #xywh.append(x)
    #xywh.append(y)
    #xywh.append(w)
    #xywh.append(h)
    #get_all_xywh_position.append(xywh)
    #print (cnt)
    #print ('x ',x,' y ',y,' w ',w,' h' ,h)
    #cv2.rectangle(cap,(x,y),(x+w,y+h),(0,255,0),2)
#print (get_all_xywh_position)
print (x_pos,y_pos,width,height)
#cv2.imshow('image',cap)
#cv2.imshow('cropped image',cap[y_pos:(y_pos+height),x_pos:(x_pos+width)])
cv2.rectangle(cap,(x_pos,y_pos),(width+x_pos,y_pos+height),(0,255,0),2)
cv2.putText(cap, 'Yellow Cable', (x_pos, height), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0),2)
cv2.imshow('cropped image',cap)
#x  91  y  352  w  354  h 389
