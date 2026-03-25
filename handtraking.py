import cv2
import mediapipe as mp
import numpy as np
import time


mpHands = mp.solutions.hands
hands = mpHands.Hands()
# for drawing the hand landmarks on the image
mpDraw = mp.solutions.drawing_utils


pTime = 0
cTime = 0

ma = cv2.VideoCapture(0)
canvas = None
prev_x, prev_y = 0, 0


def fingers_up(hand):
    fingers = []

    if hand.landmark[8].y < hand.landmark[6].y:
        fingers.append(1)
    else:
        fingers.append(0)
    if hand.landmark[12].y < hand.landmark[10].y:
        fingers.append(1)
    else:
        fingers.append(0)
    return fingers


while True:
    success, frame = ma.read()

    if canvas is None:
        canvas = np.zeros_like(frame)

    h, w, c = frame.shape

    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            x = int(handLms.landmark[8].x * w)  # 8 is the index finger tip
            y = int(handLms.landmark[8].y * h)

            fingers_up_status = fingers_up(handLms)

            if fingers_up_status[0] == 1 and fingers_up_status[1] == 0:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y

                cv2.line(canvas, (prev_x, prev_y), (x, y), (255, 0, 0), 5)
                prev_x, prev_y = x, y

            # Stop drawing
            elif fingers_up_status[0] == 1 and fingers_up_status[1] == 1:
                prev_x, prev_y = 0, 0

            # Clear canvas
            elif fingers_up_status[0] == 0 and fingers_up_status[1] == 0:
                canvas = np.zeros_like(frame)

            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    imgRGB = cv2.add(frame, canvas)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(imgRGB, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5, 
                (255, 0, 255), 3)

    cv2.imshow("Hand Tracking", imgRGB)

    if cv2.waitKey(1) == 27:
        break
ma.release()  # close camera
cv2.destroyAllWindows()  # close all windows التاب ال ظهرت
