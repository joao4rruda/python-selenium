import requests

url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=80423fcb354f45ea8fb17e14b61fc04a'

response = requests.get(url)
content = response.json()

print(type(content))
print(content['articles'][0][title])
