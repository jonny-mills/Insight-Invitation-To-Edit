#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:24:58 2019
File description:
Input: a file containing pageviews for every single Wikipedia of every day for an entire month
Processing: dataframe aggregate pageview statistics for each month are computed for each list page. Then dataframe is transposed
Output: A transposed datafrom with the rows being every single list page on Wiki, and each column is a different month of the year.
"""

import pandas as pd

df = pd.read_csv('pageviews_jan_thru_may_19.csv')
df['dates']
df['dates']=pd.to_datetime(df['dates'])
df.index = df['dates']
df = df.groupby(pd.Grouper(freq='M')).sum()
df.head()
df = df.transpose()
df.to_csv('transposed_pageviews_jan_thru_may_19.csv', sep='\t', encoding='utf-8')

