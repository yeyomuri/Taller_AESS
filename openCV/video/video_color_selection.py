import cv2
import numpy as np

def empty(a):
	pass
	
	
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

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)

cv2.createTrackbar('Hue min', 'TrackBars', 150, 179, empty)
cv2.createTrackbar('Hue max', 'TrackBars', 179, 179, empty)
cv2.createTrackbar('Sat min', 'TrackBars', 43, 255, empty)
cv2.createTrackbar('Sat max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Val min', 'TrackBars', 83, 255, empty)
cv2.createTrackbar('Val max', 'TrackBars', 255, 255, empty)

cap = cv2.VideoCapture(0)
while True:
	_, frame = cap.read()
	imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	h_min = cv2.getTrackbarPos('Hue min', 'TrackBars') #get the value
	h_max = cv2.getTrackbarPos('Hue max', 'TrackBars')
	s_min = cv2.getTrackbarPos('Sat min', 'TrackBars')
	s_max = cv2.getTrackbarPos('Sat max', 'TrackBars')
	v_min = cv2.getTrackbarPos('Val min', 'TrackBars')
	v_max = cv2.getTrackbarPos('Val max', 'TrackBars')
	print('hmin: ', h_min, ', ', 'h_max: ', h_max, ', ', 's_min: ', s_min, ', ', 's_max: ', s_max, ', ', 'v_min: ', v_min, ', ','v_max: ', v_max)
	lower = np.array([h_min, s_min, v_min])
	upper = np.array([h_max, s_max, v_max])
	mask = cv2.inRange(imgHSV, lower, upper)
	result = cv2.bitwise_and(frame, frame, mask = mask)
# 	cv2.imshow('Result', result)
# 	cv2.imshow('Espacio HSV', imgHSV)
# 	cv2.imshow('Frame', img)
# 	cv2.imshow('Mask', mask)
	imgStack = stackImages(0.6, ([frame, imgHSV], [mask, result]))
	cv2.imshow('Stacked Images', imgStack)
	cv2.waitKey(1)
	
#Libera la camara
cap.release()
#Se cierran todas las ventanas 
cv2.destroyAllWindows()
	




