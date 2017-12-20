import spotipy
import pprint
import requests
import datetime
import credentials
import sys

from spotipy.client import SpotifyException
from tinydb import TinyDB
from spotipy.oauth2 import SpotifyClientCredentials

query = sys.argv[1]
database_name = sys.argv[2]
dump_cap = sys.argv[3]
max_limit = 50
status_ok = 200
playlists = []

client_cred = SpotifyClientCredentials(
    client_id = credentials.client_creds['client_id'],
    client_secret = credentials.client_creds['client_secret']
)
db = TinyDB(database_name)
api = spotipy.Spotify(client_credentials_manager = client_cred)
results = api.search(q=query,limit=max_limit, type='playlist')

while results['playlists']['next']:
    for track in results['playlists']['items']:
        href = track['tracks']['href']
        headers = {'Authorization': 'Bearer ' + client_cred.get_access_token()}
        req = requests.get(href, headers= headers)

        if track and req.status_code == status_ok and req.json()['items']:
            playlists.append({'playlist':track, 'tracks':req.json()['items']})

        if len(playlists) >= dump_cap:
            db.insert_multiple(playlists)
            playlists = []
