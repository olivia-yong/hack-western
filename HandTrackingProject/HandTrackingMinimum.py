import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0);

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

# prevX = 0
# prevY = 0

fingerCoordinates = []

while True:  # infinite loop
    success, img = capture.read()  # creates image from videocam
    # print(img.shape[0], img.shape[1]);              # height: 480, width: 640
    # img = cv2.resize(img, (640*2, 480*2))          # increase size of video
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)  # processing hand detection
    # print(results.multi_hand_landmarks)

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
                    # cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

                if id == 8:
                    id8x = cx
                    id8y = cy
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

                # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        if ((abs(id4x - id8x)) < fingerSens) and (abs(id4y - id8y) < fingerSens):
            fingerCoordinates.append([id8x, id8y])

    for i in fingerCoordinates:
        # cv2.line(img, (i[0], i[1]), (prevX, prevY), (255, 0, 0), 2);   #testing with lines
        # prevX = i[0];
        # prevY = i[1];
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 0), cv2.FILLED)

    # fps calculation:
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # print(fps);
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 255, 0), 3)

    cv2.imshow("Image", img)  # creates window
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.waitKey(1)  # shows video
