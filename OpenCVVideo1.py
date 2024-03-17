import cv2
import numpy as np
captura = cv2.VideoCapture("TRIM_20171218_172020.mp4")

while True:
    ret, frame = captura.read() #captura del video cuadro por cuadro
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cada cuadro cambiado a gris
    cv2.imshow("video", gris) #se muestra el cuadro resultante
    if cv2.waitKey(0) == ord("e"):
        break;
captura.release() #se libera la captura
cv2.destroyAllWindows()
