import requests
from bs4 import BeautifulSoup
from connect import db


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

movies = soup.select('.ipc-metadata-list-summary-item')

# ipc-title-link-wrapper
# hrgukm
for movie in movies:
    movie_title = movie.select_one('.ipc-title__text').text
    movie_year=movie.select_one('.feoqjK > span').text
    movie_rating=movie.select_one('.ipc-rating-star').text
    doc={
        "title": movie_title,
        "year": movie_year,
        "rating": movie_rating
        }

    db.movies.insert_one(doc)