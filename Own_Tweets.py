import tweepy
import json
from tweepy import OAuthHandler
def process_or_store(tweet):
    print(json.dumps(tweet)) 
consumer_key = 'KsmSmJ3vUffyvkd553X767QTu'
consumer_secret = 'OrdTQNnYtxuPDlt6uYybjjpUbwy4JiwOHDaKkb65mGQRBL1ZbW'
access_token = '709325032204283904-A3M8Cbv10yn3mcSI9SraEvaMXFTVp3C'
access_secret = '5oW8soaCwdGCklcC1Xs3tVUs4HfsdKWE5vUtSxRN6L47i'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
    print "\n\n"
