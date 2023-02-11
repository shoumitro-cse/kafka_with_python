# https://kafka-python.readthedocs.io/en/master/usage.html
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json


#bootstrap_servers=['localhost:39092'] # works fine for kafka cluster(single node connection) 
#bootstrap_servers=['localhost:29092'] # works fine for kafka cluster(single node connection) 

bootstrap_servers=['localhost:29092', 'localhost:39092'] # works fine for kafka cluster(load balancing) 


producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Asynchronous by default
future = producer.send('my-topic', b'raw_bytes')

# Block for 'synchronous' sends
try:
	record_metadata = future.get(timeout=10)
	# Successful result returns assigned partition and offset
	print (record_metadata.topic)
	print (record_metadata.partition)
	print (record_metadata.offset)
	print("------ end ---------")
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# produce keyed messages to enable hashed partitioning
producer.send('my-topic', key=b'foo', value=b'bar')

# encode objects via msgpack
#producer = KafkaProducer(value_serializer=msgpack.dumps)
#producer.send('msgpack-topic', {'key': 'value'})

# produce json messages
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer.send('json-topic', {'key': 'value'})

# produce asynchronously
for i in range(10):
    producer.send('my-topic', {'key': i+1})

def on_send_success(record_metadata):
    print("----------------")
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)
    print("----------------\n")

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks
producer.send('my-topic', {'data': "Hello"}).add_callback(on_send_success).add_errback(on_send_error)
producer.send('my-topic', {'data': "Hello multiple retries"}).add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5, bootstrap_servers=bootstrap_servers, value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer.send('my-topic', {'data': "Hello multiple retries"}).add_callback(on_send_success).add_errback(on_send_error)

# producer.flush()



