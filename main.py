import requests
from bs4 import BeautifulSoup

# year = input("What year would you like the music to be from?\nYYYY-MM-DD: ")

# res = requests.get(f"https://billboard.com/charts/hot-100/{year}")
res = requests.get(f"https://billboard.com/charts/hot-100/2000-08-12")
web_page = res.text

soup = BeautifulSoup(web_page, "html.parser")
song_titles = [title.get_text().strip()
               for title in soup.select("ul li h3.c-title")]

print(song_titles)
