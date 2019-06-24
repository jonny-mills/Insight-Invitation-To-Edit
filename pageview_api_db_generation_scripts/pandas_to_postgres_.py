#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:53:30 2019

@author: Jonny
Sending API dataframe output from pandas into PostGreSQL database. File purpose is mainly used to test the connection between two different servers.
"""
import pandas as pd

df = pd.read_csv('clickstream_pv_may_0.csv')
from sqlalchemy import create_engine
engine = create_engine('postgresql://test1:test1@ec2-54-214-224-129.us-west-2.compute.amazonaws.com:5431/test1')
df.to_sql('1', engine)
