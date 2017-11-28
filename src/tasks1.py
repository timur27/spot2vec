import spotipy
from oauth import get_api_client
from spotipy.client import SpotifyException
import pprint
import requests

def main():
    api = get_api_client()
    name = 'a*'
    results = api.search(q='50 Cent',limit=1, type='playlist')
    

    pprint.pprint(results)

    for track in results['playlists']['items']:
        pprint.pprint(track['name'] + ', ' + track['id'])
        href = track['tracks']['href']
        req = requests.get(href)
        req.json()
        pprint.pprint(req)
    
