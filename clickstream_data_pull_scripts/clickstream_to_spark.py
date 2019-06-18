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


#datasource = "s3a://wiki-data-123456/clickstream"

def create_agg_clickstream_list(datasource):
  df = spark.read.option("delimiter", "\t").csv(datasource)
  df = df.where(df._c0.contains('List_of_'))
  #df = df.withColumn("_c3", df["_c3"].cast(IntegerType()))
  xx= df.groupBy("_c0").agg(sum('_c3'),avg('_c3')).orderBy('sum(_c3)', ascending=False)

  oldColumns = xx.schema.names
  newColumns = ["List_name", "clickview_sum","clickview_avg"]
  df = reduce(lambda xx, idx: xx.withColumnRenamed(oldColumns[idx], newColumns[idx]), xrange(len(oldColumns)), xx)
  df = df.withColumn('impact_score', df.clickview_sum/df.clickview_avg)
  df = df.orderBy(df.impact_score,ascending=False)
  return(df)

df = create_agg_clickstream_list('s3a://wiki-data-123456/clickstream')
conn = sparktopostgres.PostgresConnector()
conn.write(df,"clickstream_impact_score_may","append")
