import os

# import datetime module
import datetime
# import pymongo module
import pymongo
# connection string
client = pymongo.MongoClient("mongodb+srv://MongoDBUser:vandyHacks123!@queuedup-8aqrb.gcp.mongodb.net/test?retryWrites=true&w=majority")

# test
db = client['SampleDatabase']
# define collection
collection = db['SampleCollection']
# sample data
document = {'album': u'Melodrama', 'artist': u'Lorde', 'song': u'Green Light', 'url': 'https://music.apple.com/us/album/green-light/1428764777?i=1428766615', 'time_added': 1572709271, 'fingerprint': 'lorde_green-light', 'year': u'2017', 'do_download': True, 'album_art': 'https://is2-ssl.mzstatic.com/image/thumb/Music118/v4/83/e9/20/83e92072-972e-5715-d949-756f87dae99b/00602557725087.rgb.jpg/804x0w.jpg'}
# insert document into collection


def addToDB(document):
	collection.insert_one(document).inserted_id

def download_song(fingerprint, song, artist):
	os.system('youtube-dl --extract-audio --audio-format mp3 -o "songs/{}.%(ext)s" "ytsearch:{} {} lyrics"'.format(fingerprint, artist, song))

if __name__ == '__main__':
	download_song("thisSong.mp3", "turn down for what", "lil jon")
