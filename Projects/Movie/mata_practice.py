from bs4 import BeautifulSoup  # type: ignore
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
data = requests.get(
    "https://www.imdb.com/title/tt0068646/?ref_=chttp_t_2", headers=headers
)

soup = BeautifulSoup(data.text, "html.parser")
og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

image = og_image["content"]
title = og_title["content"]
description = og_description["content"]

print(image)
print(title)
print(description)
