import numpy as np
import cv2
import time
from kafka import KafkaProducer
import time
import datetime
import csv
import json

from keras.preprocessing import image as image_utils
import numpy as np
from keras.models import load_model

classifier = load_model('test')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 64)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 64)
producer = KafkaProducer(bootstrap_servers='52.199.170.216:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))


while(True):
	ret, gray = cap.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.resize(gray, dsize=(64, 64), interpolation=cv2.INTER_CUBIC)
	time.sleep(0.2)
	cv2.imshow('frame', gray)
	gray = image_utils.img_to_array(gray)
	gray = np.expand_dims(gray, axis=0)
	#producer.send('camera', {'user':'user-1', 'Ans': result, 'datetime':dt})
	#cv2.imshow('frame',gray)
	dt = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-4])
	result = classifier.predict(gray)
	#time.sleep(2)
	result.astype(int)
	a = result[0][0]
	print("a:",a)
	print(type(a))
	a = str(a)
	producer.send('camera', {'user':'new', 'Ans': a,'Datetime':dt})
	print("result :",result[0][0])
	#print("result1:",result[1])
	#time.sleep(2)
	#print(result)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
