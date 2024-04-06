import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

movies = soup.select('.ipc-metadata-list-summary-item')

# ipc-title-link-wrapper
# hrgukm
for movie in movies:
    movie_title = movie.select_one('.ipc-title > a').text
    movie_year=movie.select_one('.hrgukm > span').text
    movie_rating=movie.select_one('.ipc-rating-star').text
    print(movie_title.split('.')[1]," / "+movie_year+" / "+movie_rating)
  
  
# soup.select('tag name')
# soup.select('.class name')
# soup.select('#ID name')

# soup.select('upper tag name> sub tag name> sub tag name')
# soup.select('higher tag name.class name> subtag name.class name')

# # How to find by tag and attribute value
# soup.select('tag name[attribute="value"]')

# # If you only want to bring one
# soup.select_one('same as above')