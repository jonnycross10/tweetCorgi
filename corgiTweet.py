import requests
import json


randurl = "https://dog.ceo/api/breed/pembroke/images/random"

r = requests.get(randurl)

img = json.loads(r.text)
print(img['message'])
