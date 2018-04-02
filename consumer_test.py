from kafka import KafkaProducer,KafkaConsumer

import time
import datetime
import csv
import json


consumer = KafkaConsumer(bootstrap_servers='52.199.170.216:9092',
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)


consumer.subscribe(['camera'])


for message in consumer:
	print(message.value)
	print(message.value[24])

consumer.close()
