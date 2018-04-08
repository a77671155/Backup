from kafka import KafkaProducer,KafkaConsumer
import os
import time
import datetime
import csv
import json

while True:
	flag = 0
	count = 0
	print("0000")
	consumer = KafkaConsumer('camera',bootstrap_servers=['52.199.170.216:9092'])
	consumer.subscribe(['camera'])
	list = [0,0,0,]
	#print("1111")
	for message in consumer:

		print("message.value :",message.value[-5])
		a = message.value[-5]
		a = int(a)
		print("a :", a)
		list.append(a)
		print(list)
		list.pop(0)
		print(list)
		count=list.count(1)
		print("count: ",count) 
		if list.count(1) > 2:
			print("tired")
			print("list :",list)
			os.system("./music_script.sh")		
		print(message.value)
		print('ans:',message.value[-5])	
	

consumer.close()
