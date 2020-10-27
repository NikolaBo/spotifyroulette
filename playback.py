import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

def print_playlists(playlists):
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
print_playlists(playlists)

# Get random playlist
index = random.randrange(0, total)
id = ids[index]
playlist_name = playlists[index][1]['name']
playlist_items = sp.playlist_items(id)

track_name = playlist_items['items'][0]['track']['name']
uri = playlist_items['items'][0]['track']['uri']

print("Now playing track", track_name, "from your playlist", playlist_name)
print(uri)

sp.start_playback(context_uri=playlists[index][1]['uri'])

"""track = sp.current_user_playing_track()
if (track["is_playing"]):
    sp.pause_playback()
else:
    sp.start_playback()"""