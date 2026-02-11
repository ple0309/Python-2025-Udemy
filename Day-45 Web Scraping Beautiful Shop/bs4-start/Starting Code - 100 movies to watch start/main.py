import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

title_tag = soup.find_all(name="h3", class_="title")
title_lists = [item.text for item in title_tag]

#to do reverse
movies = title_lists[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")