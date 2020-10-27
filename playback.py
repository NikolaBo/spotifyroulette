import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

def print_playlists(playlists, ids):
    for idx, item in playlists:
        print(idx, item['name'], item['id'])
        ids[idx] = item['id']
    print()

# Authenticate with necessary scopes
scope = "user-read-playback-state user-modify-playback-state playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_playlists() # Get user playlist info

# Get number of playlists
total = results['total']
limit = results['limit']
if (total > limit): size = total
else: size = limit

# Print playlists and indexes
ids = [""] * total
playlists = list(enumerate(results['items'])) # Store playlist in list of tuples (index, playlist dictionary)
print_playlists(playlists, ids)

# Get random playlist
playlist_index = random.randrange(0, total)
playlist = playlists[playlist_index][1]
# Just examples
playlist_id = playlist['id']
playlist_name = playlist['name']

track_index = random.randrange(0, playlist['tracks']['total'])

sp.start_playback(context_uri=playlist['uri'], offset={"position": track_index})
sp.shuffle(state=True)
print("Currently playing track", sp.current_user_playing_track()['item']['name'], "from your playlist", playlist_name)