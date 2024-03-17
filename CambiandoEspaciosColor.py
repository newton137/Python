import cv2
import numpy as np
colores = [c for c in dir(cv2) if c.startswith("COLOR_")]
print(colores)
imagen = cv2.imread("creator.png")
while 1:
    hsv = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
    lowerVerde = np.array([0,50,200])
    upperVerde = np.array([25,255,255])
    lowerRosa = np.array([125,50,0])
    upperRosa = np.array([167,255,50])  
    mask = cv2.inRange(hsv,lowerVerde,upperVerde)
    mask2 = cv2.inRange(hsv,lowerRosa,upperRosa)
    bola = cv2.bitwise_and(imagen,imagen,mask = mask)
    camiseta = cv2.bitwise_and(imagen,imagen,mask = mask2)
    cv2.imshow("Imagen", imagen)
    cv2.imshow("Mask",mask)
    cv2.imshow("Bola",bola)
    cv2.imshow("Camiseta",camiseta)
    key = cv2.waitKey(0)
    if key == ord("b"):
        break;
cv2.destroyAllWindows()