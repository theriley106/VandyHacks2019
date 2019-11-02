# VandyHacks2019

## Random Notes

```
flask app
	add song api endpoint
		post request that takes in a song and posts the data to mongodb
			tells the web app to update from the socket
	remove song api endpoint
		post request that removes song after playing on web app
	index endpoint
		loads index.html -> this is a web app that displays songs with their order
			web socket that reloads every 5 seconds with song order

functions
	function that pulls data from mongodb and keeps track of song order
		give unique identifier to song
	function that parses spotify
	function that parses apple music
	function that downloads songs given artist and song name
		maybe unique identifier.mp3 could be song name?

swift app
	share extension to send post request with song url to server
```