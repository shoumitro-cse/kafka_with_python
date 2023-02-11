# https://kafka-python.readthedocs.io/en/master/usage.html
from kafka import KafkaConsumer
import json


#bootstrap_servers=['localhost:39092'] # works fine for kafka cluster(single node connection) 
#bootstrap_servers=['localhost:29092'] # works fine for kafka cluster(single node connection) 


bootstrap_servers=['localhost:29092', 'localhost:39092'] # works fine for kafka cluster(load balancing) 
	    
	    
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('my-topic',
                         group_id='my-group',
                         bootstrap_servers=bootstrap_servers)


for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

print("Here!")

# consume earliest available messages, don't commit offsets
consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest', enable_auto_commit=False)


# consume json messages
consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers, value_deserializer=lambda m: json.loads(m.decode('ascii')))


# consume msgpack
# consumer = KafkaConsumer(value_deserializer=msgpack.unpackb, bootstrap_servers=bootstrap_servers)


# StopIteration if no message after 1sec
consumer = KafkaConsumer(consumer_timeout_ms=1000, bootstrap_servers=bootstrap_servers)


# Subscribe to a regex topic pattern
consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
consumer.subscribe(pattern='^awesome.*')


# Use multiple consumers in parallel w/ 0.9 kafka brokers
# typically you would run each on a different server / process / CPU
consumer1 = KafkaConsumer('my-topic',
                          group_id='my-group',
                          bootstrap_servers=bootstrap_servers)
                          
consumer2 = KafkaConsumer('my-topic',
                          group_id='my-group',
                          bootstrap_servers=bootstrap_servers)
                          



