from flask import Flask, render_template, request, url_for, redirect, Markup, jsonify, make_response, send_from_directory, session
import musicController

app = Flask(__name__, static_url_path='/static')


songController = musicController.controller()

for val in musicController.EXAMPLE_SONGS:
	songInfo = musicController.parseURL(val)
	songController.add(vars(songInfo))

for i, val in enumerate(songController.order):
	print("{} - {}".format(i, val['song']))

for i in range(5):
	song = songController.play_next()
	print("Playing: {} | Next Song: {}".format(song, songController.get_next()))


@app.route('/addSong', methods=["POST"])
def index():
	data = request.get_json()
	url = data['url']
	returnedData = parseURL(url, download=True)
	return jsonify(returnedData.return_values())
	print request.get_json()
	return jsonify(data)

@app.route('/playSong', methods=["GET"])
def play_next_song():
	return "playing next song"

@app.route('/test', methods=['GET'])
def testPage():
	return render_template("index1.html")

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)