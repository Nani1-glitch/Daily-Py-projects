import numpy as np
import cv2
from collections import deque

def setValues(x):
    print("")

cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180, setValues)
cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255, setValues)
cv2.createTrackbar("Upper Value", "Color detectors", 255, 255, setValues)
cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180, setValues)
cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255, setValues)
cv2.createTrackbar("Lower Value", "Color detectors", 49, 255, setValues)


bpoints = [deque(maxlen = 1024)]
gpoints = [deque(maxlen = 1024)]
rpoints = [deque(maxlen = 1024)]
ypoints = [deque(maxlen = 1024)]

blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0


kernal = np.ones((5,5), np.uint8)

colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
colorIndex = 0

paintWindow = np.zeros((471,636,3)) + 255

cv2.namedWindow('Paint',cv2.WINDOW_AUTOSIZE)

cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
    u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
    u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
    l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
    l_saturation = cv2.getTrackbarPos("Lower saturation", "Color detectors")
    l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")

    Upper_hsv = np.array([u_hue, u_saturation, u_value])
    Lower_hsv = np.array([l_hue, l_saturation, l_value])


frame = cv2.rectangle(frame,(40,1),(140,65),(122,122,122), -1)
frame = cv2.rectangle(frame,(160,1),(255,65),colors[0], -1)
frame = cv2.rectangle(frame,(275,1),(370,65),colors[1], -1)
frame = cv2.rectangle(frame,(390,1),(485,65),colors[2], -1)
frame = cv2.rectangle(frame,(505,1),(600,65),colors[3], -1)











































    


        
