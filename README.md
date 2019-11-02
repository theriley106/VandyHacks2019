# VandyHacks2019

## Random Notes

flask app
	add song api endpoint
		post request that takes in a song and posts the data to mongodb
			tells the web app to update from the socket
	remove song api endpoint
		post request that removes song after playing on web app
	index endpoint
		loads index.html -> this is a web app that displays songs with their order
			web socket that reloads every 5 seconds with song order