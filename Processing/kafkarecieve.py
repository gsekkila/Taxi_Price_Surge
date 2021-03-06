import sys
import numpy as np
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.context import SQLContext
import json

def save_rdd(rdd):
    if not rdd.isEmpty():
        df = rdd.toDF()
        df.show()
        df.write.format("org.apache.spark.sql.redis").option("table", "location").option("key.column", "_1").save(mode='append')


zkQuorum = "10.0.0.14:9092"
topic = "location"

spark = SparkSession.builder.appName("Location").getOrCreate()
sc = spark.sparkContext
ssc = StreamingContext(sc,10)
sqlContext=SQLContext(sc)

kvs = KafkaUtils.createDirectStream(ssc,[topic], {"metadata.broker.list":zkQuorum})

#kvs.pprint()
parsed = kvs.map(lambda x: json.loads(x[1]))
data = parsed.map(lambda y: y.translate({ord(x):None for x in '[]'}))
data = data.map(lambda y: y.split(','))
#data.saveAsTextFiles("coordinates","txt")
#data = data.map(lambda x: np.array(x))
#data = data.map(lambda x: np.asfarray(x,float))
lat = data.map(lambda x: x[0])
long = data.map(lambda x:x[1])

data.pprint()
data.foreachRDD(lambda rdd: rdd.toDF().write.format("org.apache.spark.sql.redis").option("table","location").option("key.column","_1").save(mode='append'))

ssc.start()
ssc.awaitTermination()
