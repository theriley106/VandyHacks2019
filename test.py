
import time
import random
import requests
for urlVal in random.shuffle(open("demoTracks.txt").read().split("\n")):
	for i in range(random.randint(1, 5)):

		headers = {
		    'Content-Type': 'application/json',
		}

		data = {
		  'url': urlVal
		}

		response = requests.post('http://35.238.41.48:8000/addSong', headers=headers, json=data)
		print response.text
		time.sleep(.2)


