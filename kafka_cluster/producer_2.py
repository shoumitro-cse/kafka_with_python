from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import json
from time import sleep  


def my_func():   
	my_producer = KafkaProducer(  
					#bootstrap_servers=['localhost:39092'], # works fine for kafka cluster(single node connection) 
					#bootstrap_servers=['localhost:29092'], # works fine for kafka cluster(single node connection) 
					bootstrap_servers=['localhost:29092', 'localhost:39092'], # works fine for kafka cluster(load balancing) 
					value_serializer = lambda x:json.dumps(x).encode('utf-8'),  
				 )
	print("Sending......")
	for n in range(10):  
		my_data = {'num' : n}  
		my_producer.send('chatting', value = my_data)  
		sleep(2)   
	print("Sending done!")
	return "consumer_2 sms send success done!"


print(my_func()) # for consumer_2




