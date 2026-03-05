import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hand.HandDetector()
while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.detect(rgb_frame)
    hand = output.multi_hand_landmarks
    print(hand)
    cv2.imshow('Virtual_mouse', frame)
    cv2.waitKey(1)