import json
import os

import spotipy

from oauth import get_api_client

def playlist_generator(term, search_type='query',
                       offset=0, limit=50):
    api = get_api_client()
    results = api.search(term, type='playlist', offset=offset,
                             limit=limit)
        
    playlists=results['playlists']['items']

    for playlist in playlists:
        resolve_playlist(playlist['owner']['id'],
                               playlist['id']) 
        return True
    
def resolve_playlist(user_id, playlist_id):
    api = get_api_client()

    playlist_tracks = api.user_playlist_tracks(user_id, playlist_id, limit=50)

    tracks = []
    
    for track in playlist_tracks['items']:
            tracks.append(track['track']['id'])

    track_to_json(user_id, playlist_id, tracks)


def track_to_json(user_id,playlist_id,artist_sentence):
    obj = json.dumps({
        'user_id': user_id,
        'playlist_id': playlist_id,
        'sentence': artist_sentence,
        })

    print(obj)

def main(argv=None):
    print('s')
    playlist_generator('a')
