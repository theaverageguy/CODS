import time
import tweepy

auth = tweepy.OAuthHandler("KsmSmJ3vUffyvkd553X767QTu", "OrdTQNnYtxuPDlt6uYybjjpUbwy4JiwOHDaKkb65mGQRBL1ZbW")
auth.set_access_token("709325032204283904-A3M8Cbv10yn3mcSI9SraEvaMXFTVp3C", "5oW8soaCwdGCklcC1Xs3tVUs4HfsdKWE5vUtSxRN6L47i")

api = tweepy.API(auth)

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="karanjohar").pages():
    ids.extend(page)
    time.sleep(60)

screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]