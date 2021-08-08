import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    #Captura las imagenes de la camara
    _, frame = cap.read()
    #Desenfoque Gaussiano
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    
    #Convertimos nuestras de BGR a HSV
    frameHSV = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    
    #Definimos los rangos de color HSV
    lowerBlue = np.array([80, 60, 20])
    upperBlue = np.array([130, 255, 255])
    
    #Establecemos la mascara en funcion de los rangos y la imagen HSV
    frameMask = cv2.inRange(frameHSV, lowerBlue, upperBlue)
    
    #Devuelve los contornos de la mascara
    contours, _ = cv2.findContours(frameMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #Dibuja los contornos
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    
    
    
    cv2.imshow('video', frame)
    #cv2.imshow('hsv', frameHSV)
    cv2.imshow('mask', frameMask)
    #Si se presiona la tecla 'q' se saldra del bucle
    if cv2.waitKey(1000) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    