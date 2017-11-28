import json
import os
import requests

import spotipy

from oauth import get_api_client
from spotipy.client import SpotifyException

def playlist_generator(term, search_type='query',
                       offset=0):
    api = get_api_client()
    results = api.search(term, type='playlist', offset=offset)
        
    playlists=results['playlists']['items']

    for playlist in playlists:
        resolve_playlist(playlist['owner']['id'],
                               playlist['id']) 
        return True
    
def resolve_playlist(user_id, playlist_id):
    api = get_api_client()
    
    while (True):
        playlist_tracks = api.user_playlist_tracks(user_id, playlist_id, limit=50)
        for track in playlist_tracks['items']:
            print(track['track']['id'])
        
        

def track_to_json(user_id,playlist_id,track):
    obj = json.dumps({
        'user_id': user_id,
        'playlist_id': playlist_id,
        'sentence': track,
        })

    print(obj)

def main(argv=None):
    print('s')
    playlist_generator('a')
