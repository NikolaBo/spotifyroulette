# TuneRoulette
TuneRoulette is a python script that plays a random song from one of your or your friend's playlists.
## Getting started
1. Set up **Spotify Web API**.
    - In order to run the application you'll have to create an application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
    - Next, you'll need to configure a redirect uri in your application's settings. This can be whatever (eg. http://example.com).
    - Now you set up your Client Secret and Client ID as environment variables in the terminal.
        ```
        export SPOTIPY_CLIENT_ID='Your Client ID'
        export SPOTIPY_CLIENT_SECRET='Your Client Secret'
        export SPOTIPY_REDIRECT_URI='http://example.com'
        ```
     - If you're on Windows... Good luck I guess?
2. Install **spotipy**
    - `pip install spotipy`
3. Setup other users.
    - Create a text file with the IDs of each user you want to include on their own line.
    - To find a user's ID go to their profile and then Share > Copy Spotify URI. This will copy `spotify:user:the_user_id`. Simply delete the part before the ID.
    
4. Run TuneRoulette.
    - `python roulette.py`
