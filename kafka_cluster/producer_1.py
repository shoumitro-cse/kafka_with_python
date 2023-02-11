from kafka import KafkaProducer
from kafka import KafkaConsumer
from json import loads
import json
from time import sleep  


def producer_func():   
    producer = KafkaProducer(
        #bootstrap_servers=['localhost:39092'], # works fine for kafka cluster(single node connection) 
        #bootstrap_servers=['localhost:29092'], # works fine for kafka cluster(single node connection) 
        bootstrap_servers=['localhost:29092', 'localhost:39092'], # works fine for kafka cluster(load balancing) 
    )
    data = {
        'msg_data': 'Hello, How are you doing?'
    }
    serialized_data = json.dumps(data).encode('utf-8')  
    producer.send('notification', serialized_data)
    return "consumer_1 sms send success done!"


print(producer_func()) # for consumer_1   




