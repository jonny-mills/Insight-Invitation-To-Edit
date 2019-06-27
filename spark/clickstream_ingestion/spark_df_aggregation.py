"""
File description:
Input: a datasource of clickstream views for a given month of all Wikipedia pages. File size for each month ~30+ million rows.
Processing: calculating aggregate metrics for each list page in Wikipedia by grouping the category page. Agg df about 65 thousand rows
Output: PostGres receiving the aggregate clickstream dataframe.
"""

import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg, sum
from pyspark.sql.functions import lit
from pyspark.sql.types import IntegerType
import sparktopostgres
from pyspark.sql import DataFrameWriter
import os
spark = SparkSession.builder.appName("TestSpark").getOrCreate()

datasources = {'Jan':'s3a://wiki-data-123456/Jan_clickstream','Feb':"s3a://wiki-data-123456/Feb_clickstream",'March':"s3a://wiki-data-123456/March_clickstream",'April':"s3a://wiki-data-123456/clickstream_april",'May':"s3a://wiki-data-123456/clickstream",'April':"s3a://wiki-data-123456/clickstream_april",'May':"s3a://wiki-data-123456/clickstream"}


grp_window = Window.partitionBy('_c0')
magic_percentile = F.expr('percentile_approx(_c3, 0.5)')

def create_df(month, datasource):
'''Input: csv from S3
   Output: aggregate df, grouped by origin clickstream source
'''
  df = spark.read.option("delimiter", "\t").csv(datasource)
  df = df.where(df._c0.contains('List_of_'))
  df = df.where(df._c2==('link'))
  xx= df.groupBy("_c0").agg(sum('_c3'),magic_percentile.alias('med_val'),avg('_c3')).orderBy('sum(_c3)', ascending=False)
  oldColumns = xx.schema.names
  newColumns = ["list_title",month + " sum", month + " median",month+ " avg"]
  df = reduce(lambda xx, idx: xx.withColumnRenamed(oldColumns[idx], newColumns[idx]), xrange(len(oldColumns)), xx)
  return (df)


mode = "overwrite"
url = "jdbc:postgresql://10.0.0.14:5431/"
properties = {"user":"******","password":"******","driver": "org.postgresql.Driver"}

for month, datasource in datasources.items():
  print(month,datasource)
  df  = create_df(month, datasource)
