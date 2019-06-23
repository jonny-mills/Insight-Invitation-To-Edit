import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("TestSpark").getOrCreate()

'''
The purpose of this file is to ensure that spark is reading data effectively from S3.
'''
df = spark.read.text("s3a://wiki-data-123456/test.xml")
df.show()
spark.stop()
