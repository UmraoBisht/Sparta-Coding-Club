import requests

response=requests.get("http://spartacodingclub.shop/en/global_air/seoul")
responseJson=response.json()
# print(responseJson)

days=responseJson['data']['forecast']
# print(days)

for day in days:
    if day['avg'] < 100:
        print(f'{day["avg"]}=>{day["day"]}',sep='\n')