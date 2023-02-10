### Understanding the Apache Kafka
Apache Kafka is an open-source stream platform that was originally designed by LinkedIn. Later, it was handed over to Apache Foundation and open-sourced in 2011.

As per the definition from Wikipedia:

Apache Kafka is an open-source platform developed by the Apache Software Foundation used for processing streams. It is written in Java and Scala. The goal of the project is to offer a high-throughput, unified, low-latency platform in order to handle real-time data feeds. The storage layer of the Apache Kafka is fundamentally a "massively scalable pub/sub message queue designed as a distributed transaction log," that makes it extremely valuable for enterprise infrastructures in order to process streaming data. Moreover, Kafka connects to external systems (for importing and exporting data) through Kafka Connect and offers Kafka Streams, a library for Java stream processing.


### Install
```
https://www.baeldung.com/ops/kafka-docker-setup
https://www.javatpoint.com/kafka-in-python

pip install kafka-python

python producer.py # open only sms send time 
python consumer_1.py # it will have always open.
python consumer_2.py # it will have always open.
```


### Some Use Cases of Apache Kafka
### We can use Apache Kafka in different places. Let us consider some use cases of Kafka that could help us to figure out its usage:


1. Activity Monitoring:We can use Kafka to monitor activities. The activity could belong to a physical sensor and device or a website. Producers can publish raw data from data sources that can later be utilized to find trends and patterns.

2. Messaging:We can also use Kafka as a message broker among services. If we are implementing a microservice architecture, we can have a microservice as a producer and another as a consumer. For example, we have a microservice responsible for creating new accounts and sending emails to users related to account creation.

3. Log Aggregation:We can also utilize Kafka for collecting logs from distinct systems and store them in a centralized system for further processing.

4. ETL: Kafka offers a feature of almost real-time streaming; hence, we can develop an ETL based on the requirement.

5. Database:Based on things we have mentioned earlier, we can say that Kafka also acts as a database. It is not a typical database that has a feature of data querying per requirement, but Kafka can store data as long as we require without consuming it.



### Understanding the Concepts of Kafka

Let us discuss the core concepts of Kafka.

![](https://github.com/shoumitro-cse/kafka_with_python/blob/main/doc/kafka-concept.png)

Topics:Every message that is feed into the system must be part of some topic. The topic is a stream of records. The messages are store in the format of key-value pairs. Every message is assigned a sequence, known as Offset. The result of one message could be an input of the other for further processing.

Producers:Producers are the applications responsible for publishing the data into the Kafka system. They publish the data on the topic of their choice.

Consumer: There are Consumers applications that uses the messages published into topics. A consumer gets a subscription of the topic of its preference and consumes the data.

Broker: A broker is an instance of Kafka which is responsible for the message exchange. We can use Kafka as a part of a cluster or a stand-alone machine.


### What is Kafka and why it is used?
Kafka is primarily used to build real-time streaming data pipelines and applications that adapt to the data streams. 
It combines messaging, storage, and stream processing to allow storage and analysis of both historical and real-time data.


### Kafka Cluster
docker-compose -f docker-compose-kafka-cluster.yml up --build

For more stable environments, we'll need a resilient setup. A cluster setup for Apache Kafka needs to have redundancy 
for both Zookeeper servers and the Kafka servers.
https://www.tutorialspoint.com/apache_kafka/apache_kafka_cluster_architecture.htm

A Kafka cluster is a system that consists of several Brokers, Topics, and Partitions for both. The key objective is to distribute workloads equally among replicas and Partitions. Kafka Clusters Architecture mainly consists of the following 5 components: Topics. Broker.


![](https://github.com/shoumitro-cse/kafka_with_python/blob/main/doc/kafka_cluster_architecture.jpg)

The following table describes each of the components shown in the above diagram.

1. Broker

Kafka cluster typically consists of multiple brokers to maintain load balance. Kafka brokers are stateless, so they use ZooKeeper for maintaining their cluster state. One Kafka broker instance can handle hundreds of thousands of reads and writes per second and each bro-ker can handle TB of messages without performance impact. Kafka broker leader election can be done by ZooKeeper.

2. ZooKeeper

ZooKeeper is used for managing and coordinating Kafka broker. ZooKeeper service is mainly used to notify producer and consumer about the presence of any new broker in the Kafka system or failure of the broker in the Kafka system. As per the notification received by the Zookeeper regarding presence or failure of the broker then pro-ducer and consumer takes decision and starts coordinating their task with some other broker.

3. Producers

Producers push data to brokers. When the new broker is started, all the producers search it and automatically sends a message to that new broker. Kafka producer doesn’t wait for acknowledgements from the broker and sends messages as fast as the broker can handle.

4. Consumers

Since Kafka brokers are stateless, which means that the consumer has to maintain how many messages have been consumed by using partition offset. If the consumer acknowledges a particular message offset, it implies that the consumer has consumed all prior messages. The consumer issues an asynchronous pull request to the broker to have a buffer of bytes ready to consume. The consumers can rewind or skip to any point in a partition simply by supplying an offset value. Consumer offset value is notified by ZooKeeper.

