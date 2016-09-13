import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'KsmSmJ3vUffyvkd553X767QTu'
consumer_secret = 'OrdTQNnYtxuPDlt6uYybjjpUbwy4JiwOHDaKkb65mGQRBL1ZbW'
access_token = '709325032204283904-A3M8Cbv10yn3mcSI9SraEvaMXFTVp3C'
access_secret = '5oW8soaCwdGCklcC1Xs3tVUs4HfsdKWE5vUtSxRN6L47i'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
    print("\n\n")