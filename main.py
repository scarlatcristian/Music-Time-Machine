import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'
redirect_uri = "http://example.com"

year = input("What year would you like the music to be from?\nYYYY-MM-DD: ")

res = requests.get(f"https://billboard.com/charts/hot-100/{year}")
soup = BeautifulSoup(res.text, "html.parser")
song_titles = [title.get_text().strip()
               for title in soup.select("ul li h3.c-title")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private", redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret, show_dialog=True, cache_path="token.txt"
))

year = year.split('-')[0]

user_id = sp.current_user()["id"]

uris = [sp.search(title)["tracks"]["items"][0]["uri"] for title in song_titles]

playlist_id = sp.user_playlist_create(
    user=user_id, public=False, name=f"{year} BillBoard-100")["id"]
sp.user_playlist_add_tracks(playlist_id=playlist_id, tracks=uris, user=user_id)
