import spotipy
import pprint
import requests
import datetime

from spotipy.client import SpotifyException
from tinydb import TinyDB
from spotipy.oauth2 import SpotifyClientCredentials

client_cred = SpotifyClientCredentials(
    client_id='deae86cc8621462cbd5e1194c06b93ef',
    client_secret='1a6dd36a26d642879c6e36d0ac0ebb87'
)

query = 'a*'
max_limit = 50
status_ok = 200
dump_cap = 100
playlists = []
database_name = 'database.json'

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
