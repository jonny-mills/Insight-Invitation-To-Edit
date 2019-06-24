#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:50:39 2019
File description:
Input: a dataframe containing lists pages on Wikipedia that receive overall high impact scores
Processing: Randomizing the input list to select several lists for the Twitter bot to go and tweet about
Output: The bot actually tweeting to twitter with new tweets.
"""
#path="/Users/isabel/Desktop/wiki_project_june1"
import pandas as pd
from twython import Twython

df = pd.read_csv('Final_Tableau_impact_wiki3.csv')
df = df.dropna(how='any',axis=0)
list(df)
len(df)
rand_df = df.sample(n=10) 
rand_df = rand_df.reset_index(drop=True)


from auth_wiki import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


for idx in range(len(rand_df)):
    list_title = rand_df.loc[idx,'list_title_cleaned']
    url = rand_df.loc[idx,'url']
    badge = rand_df.loc[idx,'Badge']
    message = ('My algorithm has detected "' + list_title + '" to be in the top %5 of all list pages in ' +badge + "! Check out the URL to edit: " + url)
    print(message)
    twitter.update_status(status=message)
    break
    
print("Tweeted: {}".format(message))

























