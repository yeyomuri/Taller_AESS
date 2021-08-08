import cv2

img = cv2.imread('imagenes/bolas_de_color.png')

#conversion de espacios de color
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#muestra las imagenes
cv2.imshow('BGR', img)
cv2.imshow('HSV', imgHSV)
cv2.imshow('GRAY', imgGRAY)
cv2.imshow('RGB', imgRGB)

#Presiona una tecla para finalizar el programa
cv2.waitKey(0)