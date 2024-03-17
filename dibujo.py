import numpy as np
import cv2

imagen = np.zeros((512,512,3), np.uint8)#altura,ancho,(1 or 3 or 4)
imagen = cv2.line(imagen, (0, 255), (512,255), (255,0,0),4)#inicioxy,finxy,color,grosorlinea
imagen = cv2.rectangle(imagen,(210,360),(300,500),(0,0,255),3)#supizquierdo,infderecha,color,grosorlinea
imagen = cv2.circle(imagen,(255,255),100,(0,255,0),-3)#centro,radio,color,grosorlinea
imagen = cv2.ellipse(imagen,(255,105),(100,50),0,0,360,255,-1)#centro,(ejemayor,ejemenor),inclinacion,inicio,fin,transparencia,grosorlinea
puntos = np.array([[180,120],[330,120],[255,140]],np.int32)
puntos = puntos.reshape((-1,1,2))
imagen = cv2.polylines(imagen,[puntos],True,(255,0,255))#puntos,cerradoautomatico,color
fuente = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,"Texto",(50,90), fuente,10,(255,255,255),5,cv2.LINE_AA)#texto,posicion,fuente,tamaño,color,grosor,tipolinea

cv2.imshow("Imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()