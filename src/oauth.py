import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyWrapper(spotipy.Spotify):
    def category_playlists(self, category, limit=50, offset=0):
        return self._get('browse/categories/%s/playlists' % category,
                         limit=limit,
                         offset=offset)


def get_api_client():
    # create a client authentication request
    client_cred = SpotifyClientCredentials(
        client_id='deae86cc8621462cbd5e1194c06b93ef',
        client_secret='1a6dd36a26d642879c6e36d0ac0ebb87'
    )

    # create a spotify client with a bearer token,
    # dynamically re-created if necessary
    return SpotifyWrapper(auth=client_cred.get_access_token())
