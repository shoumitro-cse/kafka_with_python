# Apache Spark 
https://www.guru99.com/pyspark-tutorial.html
https://www.javatpoint.com/pyspark
https://selectfrom.dev/apache-spark-structured-streaming-via-docker-compose-3e1f146384b9
https://medium.com/@ed.bullen/spark-and-kafka-on-your-laptop-e47c5a952cd0
https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html
https://towardsdatascience.com/connecting-the-dots-python-spark-and-kafka-19e6beba6404
https://spark.apache.org/docs/2.4.0/structured-streaming-programming-guide.html # (official)
https://spark.apache.org/docs/2.4.0/structured-streaming-kafka-integration.html

# Hadoop Cluster on Docker
https://selectfrom.dev/how-to-setup-simple-hadoop-cluster-on-docker-5d8f56013f29
https://github.com/big-data-europe/docker-hadoop
https://github.com/big-data-europe/docker-hadoop/blob/master/docker-compose.yml
https://www.section.io/engineering-education/set-up-containerize-and-test-a-single-hadoop-cluster-using-docker-and-docker-compose/


# Execute kafka container with container id given above
docker exec -it kafka bash
bin/kafka-topics.sh --create --topic odom --partitions 1 --replication-factor 1 -bootstrap-server localhost:9092
/opt/bitnami/kafka/bin/kafka-topics.sh --create --topic odom --partitions 1 --replication-factor 1 -bootstrap-server localhost:9092

/opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --broker-list localhost:9092 --topic topic_1
/opt/bitnami/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --broker-list localhost:9092 --topic topic_1


# Execute zookeeper container with container id given above
docker exec -it zookeeper bash
opt/bitnami/zookeeper/bin/zkCli.sh -server localhost:2181
ls /brokers/topics # list all brokers topic



# Execute cassandra container with container id given above
docker exec -it cassandra bash

# Open the cqlsh
cqlsh -u cassandra -p cassandra

# Run the command to create 'ros' keyspace
cqlsh> CREATE KEYSPACE ros WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1};

# Then, run the command to create 'odometry' topic in 'ros'
cqlsh> create table ros.odometry(
        id int primary key, 
        posex float,
        posey float,
        posez float,
        orientx float,
        orienty float,
        orientz float,
        orientw float);
        
# Check your setup is correct
cqlsh> DESCRIBE ros.odometry



# ros => https://github.com/rospypi/simple
# pip install roslibpy
pip install --extra-index-url https://rospypi.github.io/simple/ rospy
pip install --extra-index-url https://rospypi.github.io/simple/ tf2_ros
pip install tf
pip install alpyro-msgs
# from alpyro_msgs.nav_msgs.odometry import Odometry
pip install rosinstall
pip install kafka-python pyspark


sudo pacman -Sy
yay -S python-rosinstall

# open roscore server
roscore 
http://localhost:11311/


python3 odomPublisher.py


# spark
docker exec -it spark_master bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0 streamingKafka2Console.py
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0,com.datastax.spark:spark-cassandra-connector_2.12:3.0.0 streamingKafka2Console.py


