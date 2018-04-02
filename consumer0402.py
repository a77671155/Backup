from kafka import KafkaProducer,KafkaConsumer
import os
import time
import datetime
import csv
import json

while True:
	flag = 0
	count = 0
	consumer = KafkaConsumer('camera',bootstrap_servers=['52.199.170.216:9092'])
	consumer.subscribe(['camera'])
	for message in consumer:
		flag = flag + 1
		print("flag :" ,flag)
		print("message.value :",message.value[-5])
		a = message.value[-5]
		print("a :", a)
		if a == '1':
			count = count + 1
		print("count :",count)
		if flag == 20 and count > 16 :
			print("tired")
			flag = 0
			count = 0
			os.system("echo play music")		
		print(message.value)
		print('ans:',message.value[-5])	
	

consumer.close()
