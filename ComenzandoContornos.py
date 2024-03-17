import numpy as np
import cv2

imagen = cv2.imread("creator.png")
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gris,127,255,0)
imagen2, contornos, gerarquia = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
todos = cv2.drawContours(gris,contornos,-1,(0,0,255),1)
algun = cv2.drawContours(gris,contornos,3,(255,0,0),3)
ctn = contornos[4]
imagen3 = cv2.drawContours(gris,[ctn],0,(0,255,0),5)

arreglo = [imagen,imagen2,todos,gris,imagen3]
nombres = ["imagen","imagen2","todos","algun","imagen3"]
list(map(cv2.imshow,nombres,arreglo))
cv2.waitKey(0)
cv2.destroyAllWindows()
