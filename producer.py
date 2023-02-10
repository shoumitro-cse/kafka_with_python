from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import json
from time import sleep  


def producer_func():   
    producer = KafkaProducer(bootstrap_servers='127.0.0.1:39092')
    data = {
        'msg_data': 'Hello, How are you doing?'
    }
    serialized_data = json.dumps(data).encode('utf-8')  
    producer.send('notification', serialized_data)
    return "consumer_1 sms send success done!"


def my_func():   
	my_producer = KafkaProducer(  
					bootstrap_servers = ['localhost:29092'],  
					value_serializer = lambda x:json.dumps(x).encode('utf-8'),  
				 )
	print("Sending......")
	for n in range(10):  
		my_data = {'num' : n}  
		my_producer.send('chatting', value = my_data)  
		sleep(2)   
	print("Sending done!")
	return "consumer_2 sms send success done!"


print(producer_func()) # for consumer_1   
print(my_func()) # for consumer_2




