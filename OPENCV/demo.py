import cv2
ref = cv2.imread('D:/Python/OpenCV/two.jpg')
ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
ref = cv2.threshold(ref, 230, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Image", ref)
print (ref)

