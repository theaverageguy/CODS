import tweepy 
import csv

consumer_key = "KsmSmJ3vUffyvkd553X767QTu"
consumer_secret = "OrdTQNnYtxuPDlt6uYybjjpUbwy4JiwOHDaKkb65mGQRBL1ZbW"
access_key = "709325032204283904-A3M8Cbv10yn3mcSI9SraEvaMXFTVp3C"
access_secret = "5oW8soaCwdGCklcC1Xs3tVUs4HfsdKWE5vUtSxRN6L47i"


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []  
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        
        print "...%s tweets downloaded so far" % (len(alltweets))
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    
    pass


if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("karanjohar")