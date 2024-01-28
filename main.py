import cv2
import cvzone
from cvzone.PoseModule import PoseDetector

video = cv2.VideoCapture('fall.mp4')
detector = PoseDetector()
fall_frame = 0

while True:
    _, frame = video.read()  # Read the current frame
    if frame is None:
        break  # If no frame is read, end the loop
    img = cv2.resize(frame, (1280, 720))  # Resize the frame
    result = detector.findPose(img)  # Identify standing pose
    points, bbox = detector.findPosition(img, draw=False)  # Add points to individual

    if len(points) >= 1:  # If points were recognized
        x, y, w, h = bbox['bbox']  # Save coordinates
        head = points[0][1]  # Head position
        knee = points[26][1]  # Knee position
        difference = knee - head  # Find the difference between head and knee

        if difference <= 0:  # If difference is 0 or less than 0, fall detected
            fall_frame += 1
            cvzone.putTextRect(img, 'Fall Detected', (x, y - 80), scale=2, thickness=2, colorR=(0, 0, 255))
            
            # Save the current frame as a screenshot
            if(fall_frame == 1):
                cv2.imwrite('fall_frame_screenshot.png', img)
                print("Screenshot of the video frame saved as 'fall_frame_screenshot.png'")

    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop when 'q' is pressed
        break

video.release()
cv2.destroyAllWindows()
