import cv2
import numpy as np

imagen = cv2.imread("creator.png")
imgray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,40,50,0)
img, contornos, hierarchi = cv2.findContours(thresh,1,2)
contorno = contornos[0]
envoltura = cv2.convexHull(contorno, returnPoints = False)
defectos = cv2.convexityDefects(contorno, envoltura)
for k in range(defectos.shape[0]):
    i,f,l,d = defectos[k,0]
    inicio = tuple(contorno[i][0])
    fin = tuple(contorno[f][0])
    lejos = tuple(contorno[l][0])
    cv2.line(imagen,inicio,fin,[255,0,0],2)
    cv2.circle(imagen,lejos,5,[0,255,0],-1)
cv2.imshow("Defectos", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
