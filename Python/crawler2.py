import requests
from bs4 import BeautifulSoup
# from connect import db


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.billboard.com/charts/hot-100/',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs=soup.select('.chart-results-list')

print(songs)

for song in songs:
    title=song.select_one('.o-chart-results-list-row-container > .title-of-a-story').text
    singer=song.select_one('.o-chart-results-list__item > .c-label').text
    print(title)
    print(singer)


