# cd into HandTrackingProject folder
# run this command: python .\HandTrackingMinimum.py
# ctrl + c to terminate

# library pill. specify dimensions. search jpeg to text
#imageName = "screenshotMask.jpg"

import serial
serialPort = serial.Serial(port="COM3", baudrate=19200, timeout=2)
serialString = ""
serialPort.flushInput()

import cv2
import mediapipe as mp
import time
import numpy as np

import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'
client = vision_v1.ImageAnnotatorClient()

capture = cv2.VideoCapture(0)

fingerSens = 0

def make_1080p():
    global fingerSens
    capture.set(3, 1920)
    capture.set(4, 1080)
    fingerSens = 30

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

def detectText(img):

    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)
    response = client.text_detection(image=image)
    docText = response.full_text_annotation.text
    return docText

FOLDER_PATH = r'C:\Users\xande\OneDrive\Documents\GitHub\hack-western\HandTrackingProject'
IMAGE_FILE = 'screenshotMask.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

mpHands = mp.solutions.hands
hands = mpHands.Hands()  # uses default parameters
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

id8x = 0
id8y = 0
id4x = 0
id4y = 0
id20x = 0
id20y = 0

flexValueIndex = 0
flexValueMiddle = 0

pts = []
circleSize = []

erase = False

time.sleep(0.5)

while True:  # infinite loop
    if (serialPort.in_waiting > 0):
        serialString = str(serialPort.read(2))
        serialString = serialString[2:-1]
        #print(serialString)

        if serialString[0] == chr(92):
            if serialString[1] == 'x':
                flexValueIndex = serialString[2] + serialString[3]
                flexValueIndex = int(flexValueIndex, 16)
            elif serialString[1] == 't':
                flexValueIndex = int(9)
            elif serialString[1] == 'n':
                flexValueIndex = int(10)
            elif serialString[1] == 'r':
                flexValueIndex = int(13)
            else:
                flexValueIndex = int(92)
        else:
            flexValueIndex = ord(serialString[0])

        if serialString[-1] == 'e':
            erase = True
        else:
            erase = False
        #if serialString[-5] == chr(92):
        #print(serialString[-5])
        #print(flexValueIndex)
        serialPort.flushInput()

    success, img = capture.read()  # creates image from videocam
    # print(img.shape[0], img.shape[1]);              # height: 480, width: 640
    # img = cv2.resize(img, (640*2, 480*2))          # increase size of video
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)  # processing hand detection
    # print(results.multi_hand_landmarks)

    for i in range(len(pts)):
        cv2.circle(img, pts[i], circleSize[i], (255, 0, 0), -1)

    if erase and len(pts) > 0:
        pts.pop()
        circleSize.pop()

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape  # gets height, width and channels
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(str(id) + ":", cx, cy)

                if id == 4:
                    id4x = cx
                    id4y = cy
                    #cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

                if id == 8:
                    id8x = cx
                    id8y = cy
                    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)

                if id == 20:
                    id20x = cx
                    id20y = cy

                # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        #if ((abs(id4x - id8x)) < fingerSens) and (abs(id4y - id8y) < fingerSens):
            #fingerCoordinates.append([id8x, id8y])

        if ((abs(id4x - id20x)) < fingerSens) and (abs(id4y - id20y) < fingerSens):
            cv2.imwrite('screenshotMask.jpg', mask)
            cv2.imwrite('screenshotRGB.jpg', img)
            cv2.imwrite("screenshotHSV.jpg", imgHSV)
            time.sleep(0.1)
            print(detectText(FILE_PATH))
            pts.clear()
            circleSize.clear()

        if flexValueIndex > 20:
            pts.append((id8x, id8y))
            circleSize.append(int(flexValueIndex/10))

    # Image Processing
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerBlue = np.array([0, 0, 0])
    upperBlue = np.array([200, 200, 255])
    mask = cv2.inRange(imgHSV, lowerBlue, upperBlue)
    result = cv2.bitwise_and(imgRGB, imgRGB, mask=mask)
    #cv2.imshow('HSV', imgHSV)
    #cv2.imshow('mask', mask)

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
