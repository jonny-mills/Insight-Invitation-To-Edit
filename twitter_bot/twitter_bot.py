"""
Created on Sun Jun  9 21:50:39 2019
File description:
Input: a dataframe containing lists pages on Wikipedia that receive overall high impact scores
Processing: Randomizing the input list to select lists for the Twitter bot to go and tweet about
Output: The bot actually tweeting to twitter with new tweets (using cronjob to tweet every 4 hours).
"""
import pandas as pd
from twython import Twython

df = pd.read_csv('Final_Tableau_impact_wiki3.csv') #csv too bid to upload to GH
df = df.dropna(how='any',axis=0)
rand_df = df.sample(n=2))
rand_df = rand_df.reset_index(drop=True) #must reset index after NAs are dropped

#auth_wiki not uploaded to GH due to it containing Twitter security info
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
    break #using break to only send 1 tweet, but reserving the option to tweet multiple tweets

print("Tweeted: {}".format(message))
