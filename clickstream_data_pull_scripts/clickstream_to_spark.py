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


def create_agg_clickstream_list(datasource):
  ''' Input:   Wikipedia analytics clickstream database of all wiki pages for a given month. Data is stored in S3
       Output:  A database that contains aggregate metrics and each List page in wikipedia, stored in a pyspark sql dataframe
  '''
  df = spark.read.option("delimiter", "\t").csv(datasource)
  df = df.where(df._c0.contains('List_of_'))
  agg_df= df.groupBy("_c0").agg(sum('_c3'),avg('_c3')).orderBy('sum(_c3)', ascending=False)

  oldColumns = agg_df.schema.names
  newColumns = ["List_name", "clickview_sum","clickview_avg"]
  df = reduce(lambda agg_df, idx: agg_df.withColumnRenamed(oldColumns[idx], newColumns[idx]), xrange(len(oldColumns)), agg_df)
  df = df.withColumn('impact_score', df.clickview_sum/df.clickview_avg)
  df = df.orderBy(df.impact_score,ascending=False)
  return(df)

list_of_S3_files = ['s3a://wiki-data-123456/clickstream']

for file in list_of_S3_files:
    df = create_agg_clickstream_list(file)
    conn = sparktopostgres.PostgresConnector()
    conn.write(df,"clickstream_impact_score","append")
