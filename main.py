import numpy as np
import cv2

cap = cv2.VideoCapture('videoplayback.mp4')

i=0
while(cap.isOpened()):
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('./frames/kang'+str(i)+'.jpg', frame)
    i = i + 1 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()