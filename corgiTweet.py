from secrets import consumer_key,consumer_secret, access_token, access_token_secret
from datetime import datetime
import requests
import json
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


x = True
counter = 0 #only want to run the first if statement once
while(x):
	x=datetime.now()
	h = x.strftime("%H")
	m = x.strftime("%M")
	s = x.strftime("%S")
	if (h =='08' and m == '00' and s =='00' and counter ==0):
		
		randurl = "https://dog.ceo/api/breed/pembroke/images/random"

		r = requests.get(randurl)

		img = json.loads(r.text)

		api.update_status(status = "Good morning wuv @errmalou69 " + img['message'])
		
		counter = 1
	if (h =='08' and m == '01' and s =='00'):
		counter = 0
		#this will make it so after the minute has elapsed the counter is reset
		#for the next day
		
		
