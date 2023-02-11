### Understanding the Apache Kafka
Apache Kafka is an open-source stream platform that was originally designed by LinkedIn. Later, it was handed over to Apache Foundation and open-sourced in 2011.

As per the definition from Wikipedia:

Apache Kafka is an open-source platform developed by the Apache Software Foundation used for processing streams. It is written in Java and Scala. The goal of the project is to offer a high-throughput, unified, low-latency platform in order to handle real-time data feeds. The storage layer of the Apache Kafka is fundamentally a "massively scalable pub/sub message queue designed as a distributed transaction log," that makes it extremely valuable for enterprise infrastructures in order to process streaming data. Moreover, Kafka connects to external systems (for importing and exporting data) through Kafka Connect and offers Kafka Streams, a library for Java stream processing.


### Install
```
https://www.baeldung.com/ops/kafka-docker-setup
https://www.javatpoint.com/kafka-in-python
https://pypi.org/project/kafka-python/
https://kafka-python.readthedocs.io/en/master/usage.html

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


### Apache Kafka - Fundamentals
Before moving deep into the Kafka, you must aware of the main terminologies such as topics, brokers, producers and consumers. The following diagram illustrates the main terminologies and the table describes the diagram components in detail.

![](https://github.com/shoumitro-cse/kafka_with_python/blob/main/doc/kafka_fundamentals.jpg)

In the above diagram, a topic is configured into three partitions. Partition 1 has two offset factors 0 and 1. Partition 2 has four offset factors 0, 1, 2, and 3. Partition 3 has one offset factor 0. The id of the replica is same as the id of the server that hosts it.

Assume, if the replication factor of the topic is set to 3, then Kafka will create 3 identical replicas of each partition and place them in the cluster to make available for all its operations. To balance a load in cluster, each broker stores one or more of those partitions. Multiple producers and consumers can publish and retrieve messages at the same time.

1. Topics

A stream of messages belonging to a particular category is called a topic. Data is stored in topics.

Topics are split into partitions. For each topic, Kafka keeps a mini-mum of one partition. Each such partition contains messages in an immutable ordered sequence. A partition is implemented as a set of segment files of equal sizes.

2. Partition

Topics may have many partitions, so it can handle an arbitrary amount of data.

3. Partition offset

Each partitioned message has a unique sequence id called as offset.

4. Replicas of partition

Replicas are nothing but backups of a partition. Replicas are never read or write data. They are used to prevent data loss.

5. Brokers

Brokers are simple system responsible for maintaining the pub-lished data. Each broker may have zero or more partitions per topic. Assume, if there are N partitions in a topic and N number of brokers, each broker will have one partition.

Assume if there are N partitions in a topic and more than N brokers (n + m), the first N broker will have one partition and the next M broker will not have any partition for that particular topic.

Assume if there are N partitions in a topic and less than N brokers (n-m), each broker will have one or more partition sharing among them. This scenario is not recommended due to unequal load distri-bution among the broker.

6. Kafka Cluster

Kafka’s having more than one broker are called as Kafka cluster. A Kafka cluster can be expanded without downtime. These clusters are used to manage the persistence and replication of message data.

7. Producers

Producers are the publisher of messages to one or more Kafka topics. Producers send data to Kafka brokers. Every time a producer pub-lishes a message to a broker, the broker simply appends the message to the last segment file. Actually, the message will be appended to a partition. Producer can also send messages to a partition of their choice.

8. Consumers

Consumers read data from brokers. Consumers subscribes to one or more topics and consume published messages by pulling data from the brokers.

9. Leader

Leader is the node responsible for all reads and writes for the given partition. Every partition has one server acting as a leader.

10. Follower

Node which follows leader instructions are called as follower. If the leader fails, one of the follower will automatically become the new leader. A follower acts as normal consumer, pulls messages and up-dates its own data store.



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

