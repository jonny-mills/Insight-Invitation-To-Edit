#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:53:30 2019

@author: isabel
"""
import pandas as pd
import operator
from collections import Counter
from operator import itemgetter
pd.set_option('display.max_column',None)

############################
####Loading & Cleaning DF###
############################
df = pd.read_csv('beautiful2.csv')
col = ['list_title','may_sum_clicks','may_median_clicks','may_avg_clicks','placeholder','april_sum_clicks','april_median_clicks','april_avg_clicks','placeholder1','march_sum_clicks','march_median_clicks','march_avg_clicks','placeholder2','feb_sum_clicks','feb_median_clicks','feb_avg_clicks','Placeholder3','jan_sum_clicks','jan_median_clicks','jan_avg_clicks','jan_pageviews','feb_pageviews','march_pageviews','april_pageviews','may_pageviews','Placeholder4']
df.columns = col
dropped_col = ['placeholder','placeholder1','placeholder2','Placeholder3','Placeholder4']
[df.drop(i, axis=1, inplace=True) for i in dropped_col]

print(len(df))
blacklist_words = ['porn','sex','executed','death_row']
for word in blacklist_words:
    old_len = len(df)
    df = df[~df.list_title.str.contains(word)]   
    new_len = len(df)
    print(old_len - new_len,word)

df = df[~df.list_title.str.contains('sex')]
df = df[df['may_pageviews'] != 0]
print(len(df))

df['list_title_cleaned'] = [title.replace('_',' ') for title in df['list_title']]
#df['list_title_cleaned'].head(200)
list(df)



############################
####Calc new Metrics #######
############################
def month_over_month(prev,curr):
    '''Inputs: prev is previous month's value. curr is current month's value
       Output: month/month change
    '''
    return((curr-prev)/prev)

def trend_points(growth_rate, months_ago):
    '''Inputs: growth rate is the month over month change in pageviews in a particular month. Months ago is the number of months since this particular month
       Outputs: Trending points that will go towards the trending metric
    '''
    return growth_rate / (2 ** months_ago)

def calc_trend_metric(pv_list):
    '''Input: a list of pageviews
       Output: trend metric calculated using the functions trend points and month over month
    '''
    growth_rates = []
    for i in range(len(pv_list)-1):
        growth_rates.append(month_over_month(pv_list[i+1],pv_list[i]))
    
    trend_metric = 0
    months_ago =  0
    for rate in growth_rates:
        trend_metric += trend_points(rate,months_ago)
        months_ago += 1
    #print('TREND METRIC: ', trend_metric)
    return trend_metric


##########################################
####New DF with Calculated Metrics #######
##########################################
df1 = pd.DataFrame()
df1['list_title'] = df['list_title']

df1['url'] = ['https://en.wikipedia.org/wiki/' + str(title) for title in df['list_title']]


#May_median/May_avg + April_median/April_avg, weighted towards may. a weighted average of median/avg ratio. Higher ratio indicates more ditribution across pages
df1['distribution_score'] = (df['may_median_clicks']/df['may_avg_clicks'] + df['april_median_clicks']/df['april_avg_clicks'] + df['march_median_clicks']/df['march_avg_clicks'] + df['feb_median_clicks']/df['feb_avg_clicks'] + df['jan_median_clicks']/df['jan_avg_clicks'])/5


#higher click thru rate indicates higher helpfulness
df1['helpfulness_score'] = (df['may_sum_clicks']/df['may_pageviews'] + df['april_sum_clicks']/df['april_pageviews']+ df['march_sum_clicks']/df['march_pageviews'] + df['feb_sum_clicks']/df['feb_pageviews']+ df['jan_sum_clicks']/df['jan_pageviews'])/5

df1['total_sum_clicks'] = df['may_sum_clicks'] +df['april_sum_clicks'] +df['march_sum_clicks']+df['feb_sum_clicks']+df['jan_sum_clicks']


df1['total_sum_pageviews'] = df['may_pageviews'] + df['april_pageviews']+ df['march_pageviews']+ df['feb_pageviews']+ df['jan_pageviews']


df1['trending_metric'] = df.apply(lambda x: calc_trend_metric(
            [
                    x['may_pageviews'],
                    x['april_pageviews'],
                    x['march_pageviews'],
                    x['feb_pageviews'],
                    x['jan_pageviews']
                    
             ]
        ), axis=1)

#############################
####Rank percentile DF#######
#############################
df_rank = pd.DataFrame()
df_rank['list_title'] = df['list_title']
df_rank['distribution_rank_quartile'] = df1.distribution_score.rank(pct=True)
df_rank['helpfulness_rank_quartile'] = df1.helpfulness_score.rank(pct=True)
df_rank['total_sum_clicks_quartile'] = df1.total_sum_clicks.rank(pct=True)
df_rank['total_sum_pageviews_quartile'] = df1.total_sum_pageviews.rank(pct=True)
df_rank['trending_metric_quartile'] = df1.trending_metric.rank(pct=True)
df_rank['impact_score'] = (df_rank['trending_metric_quartile'] + df_rank['total_sum_pageviews_quartile'] + df_rank['total_sum_clicks_quartile'] + df_rank['helpfulness_rank_quartile'] + df_rank['distribution_rank_quartile'])/5



df.to_csv(path_or_buf = 'cleaned_joined_wiki_data.csv', encoding='utf-8')


##############################
####Category Assignment#######
##############################

def top_words_counter(resultwords,num_reviews):
    '''Input: a list of words
       Output: a list of tuples: each tuple containing a word and its list frequency. Sorted by frequency
    '''
    counts = Counter(resultwords)
    my_dict = dict(counts)
    sorted_x = sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True)
    try:
        return (sorted_x[0:num_reviews])
    except:
        return("Not enough words")
top_words_counter(new_words,100)


top_3000_titles = list(df_rank[['list_title','impact_score']].sort_values('impact_score',ascending = False).head(3000)['list_title'])
top_3000_titles = [i.split('_') for i in top_3000_titles]
flat_list = [item for sublist in top_3000_titles for item in sublist]
stopwords = ['list','of','in','the','by']
new_words = [word for word in flat_list if word.lower() not in stopwords]


# import categories csv and create dictionary with format keyword:category
categories_dict = df_categories.set_index('keyword').to_dict()[' category']
categories_dict


import numpy as np

import numpy as np
df_rank["Category"] = np.nan
df_rank["Key"] = np.nan
df_rank['list_title']

for idx, title in enumerate(df_rank['list_title']):
    for key, value in categories_dict.items():
        try:
            if key in title.lower():
                df_rank.loc[idx,"Category"] = categories_dict[key]
                df_rank.loc[idx,"Key"] = key
                break
        except:
            break
#df_rank.info()   
#############################
####Test Queries ############
#############################
#df[df.list_title == 'List_of_birds_of_Asia'][['may_pageviews','april_pageviews','march_pageviews']]
df_rank[df_rank.list_title == 'List_of_flying_mythological_creatures'] 
df_rank[['list_title','impact_score']].sort_values('impact_score',ascending = False)
