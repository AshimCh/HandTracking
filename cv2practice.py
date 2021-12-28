import cv2
from cvzone.HandTrackingModule import HandDetector

'webcam'
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = HandDetector(detectionCon=0.8,maxHands=2)

while True:
    success,img = cap.read()
    hands,img = detector.findHands(img)
    cv2.imshow("Image",img)
    cv2.waitKey(1)

