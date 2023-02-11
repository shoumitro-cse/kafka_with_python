from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import json
from time import sleep  


def consumer_func():
    consumer = KafkaConsumer('notification', 
        #bootstrap_servers=['localhost:39092'], # works fine for kafka cluster(single node connection) 
        #bootstrap_servers=['localhost:29092'], # works fine for kafka cluster(single node connection) 
        bootstrap_servers=['localhost:29092', 'localhost:39092'], # works fine for kafka cluster(load balancing) 
        api_version=(0, 10) 
        #,consumer_timeout_ms=1000
    )
    for message in consumer:
        deserialized_data = json.loads(message.value) 
        print(deserialized_data)

consumer_func()        


