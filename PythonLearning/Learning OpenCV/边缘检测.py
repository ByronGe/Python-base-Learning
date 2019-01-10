import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.namedWindow("mywindow")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(gray,80,150)
    cv2.imshow("mywindow", edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()