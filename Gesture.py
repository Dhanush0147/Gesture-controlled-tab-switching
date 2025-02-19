import cv2
import mediapipe as mp
import pyautogui
import time

MP_HANDS = mp.solutions.hands
HANDS = MP_HANDS.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.6)
MP_DRAW = mp.solutions.drawing_utils

prev_x = None
prev_time = time.time()
MOVEMENT_THRESHOLD = 0.15  
TIME_INTERVAL = 0.5  

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        continue

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = HANDS.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            MP_DRAW.draw_landmarks(img, hand_landmarks, MP_HANDS.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark

            curr_x = landmarks[0].x
            curr_time = time.time()

            if prev_x is not None:
                time_diff = curr_time - prev_time

                if time_diff >= TIME_INTERVAL:
                    x_diff = curr_x - prev_x

                    if abs(x_diff) > MOVEMENT_THRESHOLD:
                        if x_diff > 0:
                            pyautogui.hotkey('alt', 'tab')
                        else:
                            pyautogui.hotkey('shift', 'alt', 'tab')

                    prev_x = curr_x
                    prev_time = curr_time
            else:
                prev_x = curr_x  
                prev_time = curr_time

    else:
        prev_x = None  

    cv2.imshow('HAND GESTURE RECOGNITION', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
