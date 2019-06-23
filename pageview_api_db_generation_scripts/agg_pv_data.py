#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:24:58 2019

@author: isabel
"""

import pandas as pd

df = pd.read_csv('pageviews_jan_thru_may_19.csv')
df['dates']
df['dates']=pd.to_datetime(df['dates'])
df.index = df['dates']
df = df.groupby(pd.Grouper(freq='M')).sum()
df.head()
df.transpose()


