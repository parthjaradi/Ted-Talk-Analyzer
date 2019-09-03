# -*- coding: utf-8 -*-
"""
Created on Tue May  7 01:15:50 2019

@author: Parth Jaradi
"""

import twitter

""" Setting the Authorization keys inorder to access the Twitter Account Data wihtou 
    exposing sensitive data"""

CONSUMER_KEY = '*************'
CONSUMER_SECRET = '***************************************'
OAUTH_TOKEN = '***************************************'
OAUTH_TOKEN_SECRET = '***************************************'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

def searchTweets():
    """The method diplays 20 tweets including #TedTalk """
    count = 20
    search_results = twitter_api.search.tweets(q="#TedTalk", count=count,result_type='mixed')
    statuses = search_results['statuses']
    status_text = [status['text'] for status in statuses]
    for tweet in status_text:
        print("===="*10)
        print('Tweet: ',tweet)
        print("===="*10)
        print()
#%%
