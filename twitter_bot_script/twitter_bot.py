#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:50:39 2019

@author: isabel
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
