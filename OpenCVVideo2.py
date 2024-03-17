import cv2
import numpy as np
captura = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*"DIVX")
salida = cv2.VideoWriter("nuevoVideo2.mp4", codec, 29.0, (640,480))
while captura.isOpened():
    ret, frame = captura.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        salida.write(frame)
        cv2.imshow("imagen", frame)
        if cv2.waitKey(0) == ord("e"):
            break
    else:
        break
captura.release()
salida.release()
cv2.destroyAllWindows()