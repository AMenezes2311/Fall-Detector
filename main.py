import cv2  # pip install opencv-python
import cvzone  # pip install cvzone
from cvzone.PoseModule import PoseDetector

video = cv2.VideoCapture(0)
detector = PoseDetector() 
"""
device = input('What is your device? P or C\n')
if(device == 'C'):
    h = 1280
    w = 720
else:
    h = 540
    w = 960
"""
while True:
    _, frame = video.read()  #Read the current frame
    img = cv2.resize(frame, (1280, 720))  #Resize the frame  
    resultado = detector.findPose(img)  #Identify standing pose
    pontos,bbox = detector.findPosition(img, draw=False)  #Add points to individual
    if len(pontos)>=1:  #If points were recognized
        x, y, w, h = bbox['bbox']  #Save coordinates
        cabeca = pontos[0][1]  #Head position
        joelho = pontos[26][1]  #Knee position
        diferenca = joelho-cabeca  #Find the difference between head and knee

        if diferenca <=0:  # If difference is 0 or less than 0, fall deteceted
            cvzone.putTextRect(img,'Fall Detected',(x,y-80),scale=1,thickness=1,colorR=(0,0,255))


    cv2.imshow('Video', img)
    cv2.waitKey(1)