__author__ = 'Anubhav'


#Twitter API's to extract data from twitter to extract tweets
#IMDB api to collect movies data
#Angellist api to extract startup data
#stocks data using rest api

#using REST api's or web scrapping(data collection process)

#processing happens after that

import tweepy
import json
from tweepy import OAuthHandler

CONSUMER_KEY = "BABgLwyhIiOcbSW3fY3zJ6HKW"
CONSUMER_SECRET = "076LjMi2D6uhHTSYTtMyx1y9A1IbF2VEywPfiWt52ZRrfxaZEd"
ACCESS_TOKEN = "81772439-aaJSS8cKqCoOcHwVQrgdQ5ffB0IpfRGCF4bwzqNsM"
ACCESS_TOKEN_SECRET = "YoqVeo1Ug0RG05w9lKsXC9nzJDmHD6CL6WJMjDSonhPVX"

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


friends_count=0
for friend in tweepy.Cursor(api.friends).items():
    # Process a single status
    print friend._json
    friends_count += 1

print "Friends count is  : " + str(friends_count)









