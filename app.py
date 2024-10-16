from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/index", methods=['POST'])
def search():
   with open('top_tracks_2024.json') as f:
    songs = json.load(f)
    req = request.json
    stype = req["searchBy"]
    explicit = req["explicit"]
    sort = req["sortBy"]
    term = req["term"]

    song_dict = get(stype, explicit, songs, term)
    
    if sort == 'duration':
       return jsonify(sort_by_duration(song_dict))
    elif sort == 'popularity':
       return jsonify(sort_by_popularity(song_dict))
    
    return jsonify(dict())
   
def get(type, expl, tracks, term):
   filtered = []
   for song in tracks:
      if term in song[type] and expl == song[expl]:
         filtered.add(song)

   return filtered
   


