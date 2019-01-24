import cv2
import numpy as np

img=cv2.imread('imagetest2.jpg')
blur=cv2.GaussianBlur(img,(5,5),0)
hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
#threshold green
low_g=np.array([35,100,60],np.uint8)
up_g=np.array([85,255,190],np.uint8)
mask=cv2.inRange(hsv,low_g,up_g)
mask_upstate=cv2.bitwise_and(blur, blur, mask=mask)
#get the bgr value
#mean=cv2.mean(mask_upstate)
#print (mean)

cv2.imshow('image',mask_upstate)


mean = cv2.mean(mask_upstate)
multiplier = float(mask.size)/cv2.countNonZero(mask)
mean = tuple([multiplier * x for x in mean])


