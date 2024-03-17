import cv2
import numpy as np

def funcion():
    g = imagen.copy()
    gpa = [g]
    for x in range(6):
        g = cv2.pyrDown(g)
        gpa.append(g)
    g = imagen2.copy()
    gpb = [g]
    for x in range(6):
        g = cv2.pyrDown(g)
        gpb.append(g)
    lpa = [gpa[5]]
    for x in range(5,0,-1):
        ge = cv2.pyrUp(gpa[x])
        alto, ancho = gpa[x-1].shape[:2]
        ge1 = cv2.resize(ge,(ancho,alto))
        l = cv2.subtract(gpa[x-1],ge1)
        lpa.append(l)
    lpb = [gpb[5]]
    for x in range(5,0,-1):
        ge = cv2.pyrUp(gpb[x])
        alto,ancho = gpb[x-1].shape[:2]
        ge1 = cv2.resize(ge,(ancho,alto))
        l = cv2.subtract(gpb[x-1],ge1)
        lpb.append(l)
        

imagen = cv2.imread("creator.png")
imagen2 = cv2.imread("grafo.png")
bajaPiramide = cv2.pyrDown(imagen)#se hace la imagen más chica
subePiramide = cv2.pyrUp(imagen)#se hace la imagen más grande

cv2.imshow("Baja Piramide", bajaPiramide)
cv2.imshow("Sube Piramide", subePiramide)
cv2.waitKey(0)
cv2.destroyAllWindows()