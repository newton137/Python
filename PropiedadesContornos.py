import cv2
import numpy as np

imagen = cv2.imread("creator.png",0)
ret, thresh = cv2.threshold(imagen,107,200,0)
img, contours, hierarchi = cv2.findContours(thresh,1,2)
contornos = contours[0]
x,y,w,h = cv2.boundingRect(contornos)
aspectoRadio = w/h
print(aspectoRadio)
area = cv2.contourArea(contornos)
areaRectangulo = w*h
extension = area/areaRectangulo
print(extension)
envoltura = cv2.convexHull(contornos)
areaEnvoltura = cv2.contourArea(envoltura)
solidez = area/areaEnvoltura
print(solidez)
diametroEquivalente = np.sqrt(4*area/np.pi)
print(diametroEquivalente)
izquierdo = tuple(contornos[contornos[:,:,0].argmin()][0])
derecho = tuple(contornos[contornos[:,:,0].argmax()][0])
superior = tuple(contornos[contornos[:,:,1].argmin()][0])
inferior = tuple(contornos[contornos[:,:,1].argmax()][0])
print(izquierdo,derecho,superior,inferior)
print(contornos)