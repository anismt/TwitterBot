import tweepy
import time

auth = tweepy.OAuthHandler("your_consumer_key", "your_consumer_key_secret")

auth.set_access_token("your_access_token", "your_access_token_secret")

api = tweepy.API(auth)

while True:
	api.update_status("This is the tweet you will send.")
	time.sleep(20)