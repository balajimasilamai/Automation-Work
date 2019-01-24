import cv2
import numpy as np

mser = cv2.MSER_create()
img = cv2.imread('C:/Users/balaji.ma/Desktop/Server port images/imagetest.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print (gray)
vis = img.copy()
#print (mser.detectRegions(gray))
regions, _ = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))

mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)
mask = cv2.dilate(mask, np.ones((150, 150), np.uint8))
for i, contour in enumerate(hulls):
    print (contour)
    #print (i)
    #if i == len(hulls)-1:
    #print ('len ',i)
    x,y,w,h = cv2.boundingRect(contour)
    #print (x,' ',' ',y,' ',w,' ',h)
    cv2.imshow('img',img[y:y+h,x:x+w])
    #cv2.imwrite('{}.png'.format(i), img[y:y+h,x:x+w])



cv2.imshow('img', vis)
cv2.waitKey(0)
cv2.imshow('mask', mask)
cv2.waitKey(0)
#cv2.imshow('text', text_only)
#cv2.waitKey(0)
