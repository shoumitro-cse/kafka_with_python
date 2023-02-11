#for django application
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'als_social.settings')
django.setup()
from kafka import KafkaConsumer
import json
from accounts.models.account_setting import FAQ


bootstrap_servers=['localhost:29092', 'localhost:39092'] # works fine for kafka cluster(load balancing) 
	    
	    
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('my-topic', group_id='my-group', bootstrap_servers=bootstrap_servers)


for message in consumer:
    #print ("topic=%s partition=%d offset=%d: key=%s value=%s" % (
    #      message.topic, message.partition, message.offset, message.key, message.value)
    #)
    FAQ.objects.create(question="What is kafka", answer=f"It's a message broker {str(message.value)}")
    print("FAQ insert Done!")

print("Will not reach here any time!")


                          



