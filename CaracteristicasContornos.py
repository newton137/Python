import cv2
import numpy as np

imagen = cv2.imread("creator.png",0)
ret,thresh = cv2.threshold(imagen,107,200,0)
img, contours, hierarchi = cv2.findContours(thresh,1,2)
contornos = contours[0]
momentos = cv2.moments(contornos)
print(momentos)
centrox = int(momentos["m10"]/momentos["m00"])
centroy = int(momentos["m01"]/momentos["m00"])
area = cv2.contourArea(contornos)
perimetro = cv2.arcLength(contornos,True)
print(centrox,centroy,area,perimetro)
epsilon = 0.1*cv2.arcLength(contornos,True)
aproximar = cv2.approxPolyDP(contornos,epsilon,True)
print(aproximar)
