#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:52:49 2019

@author: isabel
"""
import pandas as pd
from sqlalchemy import create_engine
import psycopg2 
import io

#engine = create_engine('postgresql://test1:test1@ec2-54-214-224-129.us-west-2.compute.amazonaws.com:5431/test1')
#df.to_sql('1', engine)
df =pd.read_csv('pageviews_jan_thru_may_2019.csv')
df['dates']
df['dates']=pd.to_datetime(df['dates'])
df.index = df['dates']
df = df.groupby(pd.Grouper(freq='M')).sum()
df.head()
df = df.transpose()
df['list_title'] =df.index



engine = create_engine('postgresql+psycopg2://test1:test1@ec2-54-214-224-129.us-west-2.compute.amazonaws.com:5431/test1')

df.head(0).to_sql('pageview_jan_may_data2', engine, if_exists='replace',index=False) #truncates the table

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'pageview_jan_may_data2', null="") # null values become ''
conn.commit()
#https://stackoverflow.com/questions/23103962/how-to-write-dataframe-to-postgres-tablenp.array([fdsf, dsfds])
