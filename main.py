import os

def download_song(fingerprint, song, artist):
	os.system('youtube-dl --extract-audio --audio-format mp3 -o "songs/{}.%(ext)s" "ytsearch:{} {} lyrics"'.format(fingerprint, artist, song))

if __name__ == '__main__':
	download_song("thisSong.mp3", "turn down for what", "lil jon")