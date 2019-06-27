#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File description:
Input: Pageview API
Processing: Calling pageview API for every Wiki list page, daily from Jan 2019 - May 2019
Output: Daily pageview data for every Wiki list page from Jan 2019 - May 2019
"""

import wikipedia as wiki
import pageviewapi
import pageviewapi.period
from collections import Counter
import pandas as pd
from timeit import default_timer as timer


#####Create a pandas df index of everyday from Jan 2019 - May 2019
from datetime import date, timedelta
dates = []
d1 = date(2019, 1, 1)  # start date
d2 = date(2019, 5, 31)  # end date
delta = d2 - d1         # timedelta
for i in range(delta.days + 1):
    a = (d1 + timedelta(days=i))
    dates.append(a)
print(dates)

df = pd.DataFrame()
df['dates'] = dates
df['dates']=pd.to_datetime(df['dates'])
df.index = df['dates']

def views(article_name,start_date,end_date):
    '''Input: a wiki article name, and the desired date range for daily pageview data to be collected
       Output: a list containing pageviews of the article for specified range
    '''
    page_views = []
    d = pageviewapi.per_article('en.wikipedia', article_name, start_date, end_date,access='all-access', agent='all-agents', granularity='daily')
    for i in range(len(d['items'])):
        page_views.append(d['items'][i]['views'])
    return(page_views)

reader = open("list_test_file.txt", "r")  #reads in file of all list pages from Wikipedia
wiki_list = reader.read().split('\n')
wiki_list_cleaned  = []
for i in wiki_list:
    wiki_list_cleaned.append(i.split('\t')[1])
    
wiki_list_cleaned = [i.replace('‚Äì',"-").replace('‚Äö√Ñ√¨',"-") for i in wiki_list_cleaned] #cleaning special chars
list_title = []
number_of_views = []


start = timer()
for idx,i in enumerate(wiki_list_cleaned): 
    print(idx)
    list_title.append(i)
    try:
        df[i] = views(i.replace('_',' '),'20190101', '20190531') #collecting data for all list pages from Jan 1 to May 31
    except:
        df[i] = None #if the API can not locate the specified list page
end = timer()
print(end - start) 

df.to_csv(path_or_buf = 'pageviews_jan_thru_may_19.csv', encoding='utf-8')






df = pd.DataFrame()
df['list_title'] = list_title
df['number_of_views'] = number_of_views
print(df)









