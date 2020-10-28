import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random
import time

def print_playlists(playlists):
    for idx, item in playlists:
        print(idx, item['name'], item['id'])
    print()


# Authenticate with necessary scopes
scope = "user-read-playback-state user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get users
user_ids = []
users = []
prompt = input("Enter a file to read users from, or 'Q' for just yourself: ")
if (prompt != "Q"):
    f = open(prompt)
    for line in f:
        try:
            L = line.strip()
            users.append(sp.user(L))
            user_ids.append(L)
        except:
            print("Could not find user:", line)

prompt = ""
# Loop through roulette until player wants to stop
while (prompt != "Q"):
    # Choose a random user and get their playlists
    random_user_index = random.randrange(0, len(user_ids) + 1)
    if (random_user_index == len(user_ids)):
        results = sp.current_user_playlists()
        user_name = "you"
    else:
        results = sp.user_playlists(user_ids[random_user_index])
        user_name = users[random_user_index]['display_name']
        print(user_name)

    # Get number of playlists
    total = results['total']
    limit = results['limit']
    if (limit < total): max = limit
    else: max = total

    # Store playlist in list of tuples (index, playlist dictionary)
    playlists = list(enumerate(results['items'])) 
    # Print playlists and indexes (for debugging or whatnot)
    #print_playlists(playlists)

    # Get random playlist
    playlist_index = random.randrange(0, max)
    playlist = playlists[playlist_index][1]
    playlist_name = playlist['name']

    # Get random track in playlist
    track_index = random.randrange(0, playlist['tracks']['total'])

    # Play track
    sp.start_playback(context_uri=playlist['uri'], offset={"position": track_index})
    sp.shuffle(state=True)

    # Tell us what's playing!!
    time.sleep(1)
    current_track = sp.current_user_playing_track()
    try:
        current_track_name = current_track['item']['name']
        if (user_name != "you"): 
            print("Now playing track", current_track_name, "from " + user_name + "'s playlist", playlist_name)
        else: 
            print("Now playing track", current_track_name, "from your playlist", playlist_name)
    except:
        print("Huh there was an error getting the current track's metadata.")
    
    prompt = input("Enter anything but 'Q' to play something new: ")