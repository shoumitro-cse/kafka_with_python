from kafka import KafkaConsumer
import json

#bootstrap_servers=["172.18.0.4:9092"]
bootstrap_servers=["0.0.0.0:9092"]	    
	    
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('topic_1', group_id='my-group', bootstrap_servers=bootstrap_servers)

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    
    #print(message)
    # ConsumerRecord(topic='my-topic', partition=0, offset=870, timestamp=1676109866735, timestamp_type=0, 
    #                key=None, value=b'raw_bytes', headers=[], checksum=None, serialized_key_size=-1, 
    #                serialized_value_size=9, serialized_header_size=-1)

    #print(message.value.decode('utf-8')) # {"key": 9} of message.value
    
    print ("topic=%s partition=%d offset=%d: key=%s value=%s" % (
          message.topic, message.partition, message.offset, message.key, message.value)
    )

print("Will not reach here any time!")




