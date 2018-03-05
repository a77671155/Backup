import numpy as np
import cv2
import time

i=5468
cap = cv2.VideoCapture('zack_untired.mp4')
#cap = cv2.VideoCapture(0)
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
#for(int i=0 ; i<10 ;i++)
while(cap.isOpened()):
  #frame = cv2.VideoCapture.read(cap)
  
  ret, frame = cap.read()
  
 
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  frames_name = "./zack/training_untired/test_%d.jpeg"%i
    
  cv2.imwrite(frames_name, gray)
  i= i+1
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()