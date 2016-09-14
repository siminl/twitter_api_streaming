import tweepy
from requests_oauthlib import OAuth1Session
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
access_token = "2331702803-xdMRaD87y1NMmVV1GZXkTAa6fi51fiQdUrzNqj1"
access_token_secret = "1j9f6D3v8mcv1x5BIXqNEsHuxaUkX7vlCejlLATI6NRjW"
consumer_key = "PnSFkzgj4Ad5tRhwbTKHO0eIO"
consumer_secret = "mM7V0VWtpiZ0f14npFPCs3IneafrE84ocUe7WhGxnn2BTA94u2"
class StdOutListener(StreamListener):

    def on_data(self, data):
 #       print data
        with  open('twitter_16_09050909.txt', 'a') as tf: tf.write(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
 #   stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords real-time
#    stream.filter(track=['IPHONE','iphone','Apple'])

    stream = tweepy.API(auth)
    for tweet in tweepy.Cursor(stream.search,q= ["IPHONE", "iphone", "Apple", "IP", "ip"], lang ="en").items():
        print tweet


######## add in parameter to narrow down the extraction #####

    
##
##    import json
##    import pandas as pd
##    import matplotlib.pyplot as plt
##    
