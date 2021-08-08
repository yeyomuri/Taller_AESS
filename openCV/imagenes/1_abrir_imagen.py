import cv2

img = cv2.imread('imagenes/bolas_de_color.png')

cv2.imshow('Frame', img)

cv2.waitKey(0)
