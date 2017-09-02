import numpy as np
import cv2

cap = cv2.VideoCapture("C:\Users\Soulbrotha\Videos\Space Ghost Season 1Episode 1      The Heat Thing.mp4") #enter video location ie "C:\Users\..)

while(cap.isOpened()):
    # Captures video frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #changes to grayscale

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
