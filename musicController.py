import requests
import bs4
import json
import time


class parseURL():
	def __init__(self, url):
		# This maps the given url to a specific function
		# AKA really bad code but okay...
		functionMap = {
			'spotify': self.parse_spotify,
			'music.apple.com': self.parse_apple_music,
			'googleplaymusic': self.parse_google_play,
			'youtube': self.parse_youtube
		}

		self.url = url

		urlParse = self.parse_error

		# this is probably the worst code/logic so far...
		for key, val in functionMap.iteritems():
			if key in url.lower():
				urlParse = val
				# lol wut
				break

		self.time_added = int(time.time())
		self.album_art = None
		self.artist = None
		self.song = None
		self.year = None
		self.album = None
		self.fingerprint = None

		urlParse()

	def gen_fingerprint(self):
		return "{}_{}".format(self.artist.replace(" ", "-"), self.song.replace(" ", "-")).lower()

	def recount(self):
		RANKING.add(vars(self))

	def parse_error(self):
		raise Exception("[CUSTOM ERROR] Error with parsing URL: {}".format(self.url))

	def parse_spotify(self):

		page = get_page_from_url(self.url)

		tempVal = split_between(str(page), "Spotify.Entity = ", '"};') + '"}'
		spotifyDoc = json.loads(tempVal)
		if 'album' in spotifyDoc:
			spotifyDoc = spotifyDoc['album']
		self.album_art = spotifyDoc["images"][0]['url']
		self.year = spotifyDoc["release_date"].partition("-")[0]
		self.artist = spotifyDoc["artists"][0]["name"]
		self.album = spotifyDoc["name"]
		self.song = page.title.string.partition(", a ")[0]
		self.fingerprint = self.gen_fingerprint()
		return

	def parse_apple_music(self):
		return

	def parse_google_play(self):
		return

	def parse_youtube(self):
		return

	def return_values(self):
		return vars(self)
