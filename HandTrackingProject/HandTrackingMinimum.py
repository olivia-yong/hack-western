# cd into HandTrackingProject folder
# run this command: python .\HandTrackingMinimum.py
# ctrl + c to terminate

# library pill. specify dimensions. search jpeg to text

import serial
#serialPort = serial.Serial(port = "COM3", baudrate=19200, timeout=2)
#serialString = ""
#serialPort.flushInput()

import cv2
import mediapipe as mp
import time
<<<<<<< Updated upstream
=======
import numpy as np
>>>>>>> Stashed changes

capture = cv2.VideoCapture(0)

fingerSens = 0

def make_1080p():
    global fingerSens
    capture.set(3, 1920)
    capture.set(4, 1080)
    fingerSens = 50

def make_720p():
    global fingerSens
    capture.set(3, 1280)
    capture.set(4, 720)
    fingerSens = 30

def make_480p():
    global fingerSens
    capture.set(3, 640)
    capture.set(4, 480)
    fingerSens = 20

make_1080p()  # change resolution

mpHands = mp.solutions.hands
hands = mpHands.Hands()  # uses default parameters
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

id8x = 0
id8y = 0
id4x = 0
id4y = 0

flexValue = 0

prevX = 0
prevY = 0

fingerCoordinates = []
circleSize = []

while True:  # infinite loop
<<<<<<< Updated upstream
    if (serialPort.in_waiting > 0):
        serialString = str(serialPort.read(2)) + "!!!!!!!!"
        if len(serialString) == 17:
            #flexValue = int(serialString[6])*10 + int(serialString[7])
            flexValue = serialString[6] + serialString[7];
            flexValue = int(flexValue, 16)
        else:
            flexValue = ord(serialString[4])
        print(flexValue)
        serialPort.flushInput()
=======
    #if (serialPort.in_waiting > 0):
        #serialString = str(serialPort.read(2))
        #serialString = serialString[2:]
        #print(serialString)
        #print(serialString[4])
        # if len(serialString) == 15:
        #     if serialString[3] == 'n':
        #         # takes the hex value in the serial string and combines them into one string
        #         flexValue = serialString[6] + serialString[7]
        #     else:
        #         flexValue = serialString[4] + serialString[5]
        #     # takes the string with integers and converts to an actual integer:
        #     flexValue = int(flexValue, 16)
        # elif len(serialString) == 13 and not serialString[3] == chr(92):
        #     character = serialString[2] + serialString[3]
        #     flexValue = ord(character)
        # else:
        #     flexValue = ord(serialString[2])

        # if serialString[0] == chr(92):
        #     if serialString[1] == 'x':
        #         flexValueIndex = serialString[2] + serialString[3]
        #         flexValueIndex = int(flexValueIndex, 16)
        #     elif serialString[1] == 't':
        #         flexValueIndex = int(9)
        #     elif serialString[1] == 'n':
        #         flexValueIndex = int(10)
        #     elif serialString[1] == 'r':
        #         flexValueIndex = int(13)
        #     else:
        #         flexValueIndex = int(92)
        # else:
        #     flexValueIndex = ord(serialString[0])
        #
        # #if serialString[-5] == chr(92):
        # print(serialString[-5])
        # #print(flexValue)
        # serialPort.flushInput()
>>>>>>> Stashed changes

    success, img = capture.read()  # creates image from videocam
    # print(img.shape[0], img.shape[1]);              # height: 480, width: 640
    # img = cv2.resize(img, (640*2, 480*2))          # increase size of video
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)  # processing hand detection
    # print(results.multi_hand_landmarks)

    for i in range(len(pts)):
        #cv2.circle(img, pts[i], circleSize[i], (255, 0, 0), -1)
        cv2.circle(img, pts[i], 10, (255, 0, 0), -1)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape  # gets height, width and channels
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(str(id) + ":", cx, cy)

                if id == 12:
                    id4x = cx
                    id4y = cy
                    #cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

                if id == 8:
                    id8x = cx
                    id8y = cy
                    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)

<<<<<<< Updated upstream
                # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        #if ((abs(id4x - id8x)) < fingerSens) and (abs(id4y - id8y) < fingerSens):
            #fingerCoordinates.append([id8x, id8y])
        if flexValue > 20:
            fingerCoordinates.append([id8x, id8y])
            circleSize.append(int(flexValue/20))

    for i in range(len(fingerCoordinates)):
        cv2.line(img, (fingerCoordinates[i][0], fingerCoordinates[i][1]), (prevX, prevY), (255, 0, 0), circleSize[i])   #testing with lines
        prevX = fingerCoordinates[i][0]
        prevY = fingerCoordinates[i][1]
        #cv2.circle(img, (fingerCoordinates[i][0], fingerCoordinates[i][1]), circleSize[i], (255, 0, 0), cv2.FILLED)
=======
                if id == 20:
                    id20x = cx
                    id20y = cy

                # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        if ((abs(id4x - id8x)) < fingerSens) and (abs(id4y - id8y) < fingerSens):
            pts.append([id8x, id8y])

        if ((abs(id4x - id20x)) < fingerSens) and (abs(id4y - id20y) < fingerSens):
            cv2.imwrite('screenshot.jpg', img)
        #if flexValueIndex > 20:
            #pts.append((id8x, id8y))
            #circleSize.append(int(flexValueIndex/10))



>>>>>>> Stashed changes

    # fps calculation:
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # print(fps);
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 255, 0), 3)

    cv2.imshow("Image", img)  # creates window
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.waitKey(1)  #shows video
