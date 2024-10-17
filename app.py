from flask import Flask, jsonify, request
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
    expl = req["explicit"]
    sort = req["sortBy"]
    term = req["term"]

   ## filter
   filtered = []
   for song in songs:
      if (term in song[stype] or song[stype].find(term) != -1) and expl == song["explicit"]:
         filtered.append(song)

   song_dict = filtered
   ##song_dict = get(stype, explicit, songs, term)
    
   ## sort
   song_dict = sorted(song_dict, key=lambda song: song[sort])
   

   ## return
   return jsonify(song_dict)   
   


