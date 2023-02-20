from pyspark.sql import SQLContext
from pyspark import SparkFiles
from pyspark import SparkContext

url = "https://raw.githubusercontent.com/guru99-edu/R-Programming/master/adult_data.csv"
sc = SparkContext()
sc.addFile(url)
sqlContext = SQLContext(sc)

df = sqlContext.read.csv(SparkFiles.get("adult_data.csv"), header=True, inferSchema= True)
df.printSchema()



