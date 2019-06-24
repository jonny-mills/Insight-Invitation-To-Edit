#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:50:39 2019
File description:
Input: a dataframe containing lists pages on Wikipedia that receive overall high impact scores
Processing: Randomizing the input list to select several lists for the Twitter bot to go and tweet about
Output: The bot actually tweeting to twitter with new tweets.
"""
path="/Users/isabel/Desktop/wiki_project_june1"
import os
os.chdir(path)

from twython import Twython

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

#a = df['list_title'].head(100)
import random
z = random.sample(list(a), 20)

for i in z:
    message = i
    twitter.update_status(status=message)
    
print("Tweeted: {}".format(message))
