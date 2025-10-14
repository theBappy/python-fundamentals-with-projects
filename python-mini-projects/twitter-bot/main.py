import tweepy
import time

print("Testing the BOT")

api_key = "enter your api key"
api_secret = "enter your api secret"
access_token = "enter your access token"
access_token_secret = "enter your access token secret"

# Creating an OAuthHandler, not a Client
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not status.retweeted and status.in_reply_to_status_id is None:
            print(status.text)
            try:
                api.retweet(status.id)
                print("Retweeted")
            except tweepy.TweepError as e:
                print(e.reason)

    def on_error(self, status_code):
        if status_code == 420:
            print("Error 420: Enhance your calm - rate limited.")
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

keywords = ["#Python", "#python", "#programming", "#coding"]
myStream.filter(track=keywords, languages=["en"])
