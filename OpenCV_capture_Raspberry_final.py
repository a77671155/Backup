import numpy as np
import cv2
import time


from keras.preprocessing import image as image_utils
import numpy as np
from keras.models import load_model

classifier = load_model('model')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 64)

while(True):
	ret, gray = cap.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
	time.sleep(0.2)
	cv2.imshow('frame', gray)
	gray = image_utils.img_to_array(gray)
	gray = np.expand_dims(gray, axis=0)
	
	#cv2.imshow('frame',gray)
	result = classifier.predict(gray)
	print(result)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()