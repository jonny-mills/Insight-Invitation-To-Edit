#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:03:12 2019

@author: Jonny
"""

import wikipedia as wiki
import pageviewapi
import pageviewapi.period
from collections import Counter
import pandas as pd

from timeit import default_timer as timer


# ...

print(end - start) # Time in seconds, e.g. 5.38091952400282

def sum_views(article_name,start_date,end_date):
    views = []
    d = pageviewapi.per_article('en.wikipedia', article_name, start_date, end_date,access='all-access', agent='all-agents', granularity='daily')
    for i in range(len(d['items'])):
        views.append(d['items'][i]['views'])
    return(sum(views))

reader = open("list_test_file.txt", "r")  ##
wiki_list = reader.read().split('\n')
wiki_list_cleaned  = []
for i in wiki_list:
    wiki_list_cleaned.append(i.split('\t')[1])
    
    
list_title = []
number_of_views = []

start = timer()
for idx,i in enumerate(wiki_list_cleaned):
    print(idx)
    list_title.append(i)
    try:
        number_of_views.append(sum_views(i.replace('_',' '),'20190401', '20190430'))
    except:
        number_of_views.append(None)
end = timer()
print(end - start) 
    

df = pd.DataFrame()
df['list_title'] = list_title
df['number_of_views'] = number_of_views
print(df)

df.to_csv(path_or_buf = 'clickstream_pv_may_0.csv', encoding='utf-8')









'''
pageviewapi.period.sum_last('en.wikipedia', 'Michelle Obama', last=0,access='all-access', agent='all-agents')

wiki.summary('Taylor Swift')
pageviewapi.period.sum_last('en.wikipedia', 'Derek Jeter', last=30,access='all-access', agent='all-agents')

pageviewapi.period.sum_last('en.wikipedia', 'Selena Gomez', last=30,access='all-access', agent='all-agents')
pageviewapi.period.sum_last('en.wikipedia', 'Tim Tebow', last=30,access='all-access', agent='all-agents')
pageviewapi.period.sum_last('en.wikipedia', 'Donald Trump', '20151106', '20151120',access='all-access', agent='all-agents')
pageviewapi.per_article('en.wikipedia', 'Paris', access='all-access', agent='all-agents', granularity='daily')

pageviewapi.period.sum_last('en.wikipedia', 'Paris', last=30)

pageviewapi.legacy_pagecounts('en.wikipedia', '2010010100', '2011010100', granularity='monthly')


#https://pypi.org/project/pageviewapi/

wiki.content('Dwayne Johnson')
wiki.geosearch('18','19')
wiki.content('Dwayne Johnson')

a = wiki.page('Emma Watson')
b= a.content.replace('\n',' ').split(' ')
c = Counter(b)
c['his']
c['her']
'''

'''
start = timer()
for i in wiki_list_cleaned[2000:2100]:
    list_title.append(i)
    try:
        z = pageviewapi.period.sum_last('en.wikipedia', i.replace('_',' '), last=45,access='all-access', agent='all-agents')
        number_of_views.append(z)
    except :
        number_of_views.append(None)
end = timer()
print(end - start)
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    