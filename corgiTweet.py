import requests
import json
import tweepy
from secrets import consumer_key,consumer_secret, access_token, access_token_secret


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



randurl = "https://dog.ceo/api/breed/pembroke/images/random"

r = requests.get(randurl)

img = json.loads(r.text)
#print(img['message'])

api.update_status(status = "WUV U @errmalou69 " + img['message'])
