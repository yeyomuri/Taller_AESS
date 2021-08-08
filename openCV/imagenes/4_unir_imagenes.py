import cv2
import numpy as np
#Funcion que une las imagenes en un arreglo
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
#--------------------------FINALIZACION DE LA FUNCION-----------------

img = cv2.imread('imagenes/bolas_de_color.png')

#conversion de espacios de color
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#muestra las imagenes
# cv2.imshow('BGR', img)
# cv2.imshow('HSV', imgHSV)
# cv2.imshow('GRAY', imgGRAY)
# cv2.imshow('RGB', imgRGB)

#Ordena las imagenes en un arreglo
imgStack = stackImages(0.9, ([img, imgHSV], [imgGRAY, imgRGB]))

#Muestra la imagen ordenada
cv2.imshow('Espacios_de_color', imgStack)

#Presiona una tecla para finalizar el programa
cv2.waitKey(0)
