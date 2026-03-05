import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hand.HandDetector()
drawing_utils = mp.solutions.drawing_utils
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.detect(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, lm in enumerate(landmarks):
                if id == 8:
                    x = landmark.x
                    y = landmark.y
                    print(x, y)
    cv2.imshow('Virtual_mouse', frame)
    cv2.waitKey(1)