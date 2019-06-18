import sys

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TestSpark").getOrCreate()

df = spark.read.text("s3a://wiki-data-123456/test.xml")
df.show()
print("Jonny")
spark.stop()
