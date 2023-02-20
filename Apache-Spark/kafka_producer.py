# https://kafka-python.readthedocs.io/en/master/usage.html
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json


#bootstrap_servers=["172.18.0.4:9092"]
bootstrap_servers=["0.0.0.0:9092"]

producer = KafkaProducer(bootstrap_servers=bootstrap_servers, value_serializer=lambda m: json.dumps(m).encode('ascii'))


messages = {
	"id": 1,
	"posex": 1.2,
	"posey": 2.2,
	"posez": 3.2,
	"orientx": 4.2,
	"orienty": 5.2,
	"orientz": 6.2,
	"orientw": 7.2,
}


# Asynchronous by default
future = producer.send('topic_1', messages)


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


