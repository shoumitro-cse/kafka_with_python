from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import json
from time import sleep  


def my_func():
	my_consumer = KafkaConsumer(  
			'message',  
			 bootstrap_servers = ['localhost : 29092'],  
			 auto_offset_reset = 'earliest',  
			 enable_auto_commit = True,  
			 group_id = 'my-group',  
			 value_deserializer = lambda x : json.loads(x.decode('utf-8'))  
		 )  
	for message in my_consumer:  
		#deserialized_data = json.loads(message.value) 
		print(message.value)
        

my_func()


