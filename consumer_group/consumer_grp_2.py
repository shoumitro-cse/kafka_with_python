from kafka import KafkaProducer, KafkaConsumer, TopicPartition
from json import loads
import json
from time import sleep  


def my_consumer_grp_2():
	TOPIC = "chatting"
	PARTITION_1 = 1
	
	consumer_1 = KafkaConsumer(
		TOPIC, 
		group_id='grp1', 
	    #bootstrap_servers=['localhost:39092'], # works fine for kafka cluster(single node connection) 
	    #bootstrap_servers=['localhost:29092'], # works fine for kafka cluster(single node connection) 
	    bootstrap_servers=['localhost:29092', 'localhost:39092'], # works fine for kafka cluster(load balancing) 
		auto_offset_reset = 'earliest',  
		enable_auto_commit = True,  
		value_deserializer = lambda x : json.loads(x.decode('utf-8'))  
	)
	
	topic_partition_1 = TopicPartition(TOPIC, PARTITION_1)
	
	# format: topic, partition
	#consumer_1.assign([topic_partition_1])
	
	#msg = next(consumer_1)
	#print(msg)
	
	for message in consumer_1:  
		print(message.value)
        

my_consumer_grp_2() # for consumer group 2



