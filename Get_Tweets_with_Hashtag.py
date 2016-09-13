from twython import Twython

TWITTER_APP_KEY = 'KsmSmJ3vUffyvkd553X767QTu' 
TWITTER_APP_KEY_SECRET = 'OrdTQNnYtxuPDlt6uYybjjpUbwy4JiwOHDaKkb65mGQRBL1ZbW' 
TWITTER_ACCESS_TOKEN = '709325032204283904-A3M8Cbv10yn3mcSI9SraEvaMXFTVp3C'
TWITTER_ACCESS_TOKEN_SECRET = '5oW8soaCwdGCklcC1Xs3tVUs4HfsdKWE5vUtSxRN6L47i'

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#omg',   
                  count=100)

tweets = search['statuses']

for tweet in tweets:
  print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
