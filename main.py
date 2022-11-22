import requests

# get api key and url from newsapi.org
api_key = '793b70fa6a734a30aab62307ede9b395'
url = "https://newsapi.org/v2/top-headlines?country=us&category=" \
      "business&apiKey=793b70fa6a734a30aab62307ede9b395"

request = requests.get(url)
# convert string into dict to extract info
content = request.json()
print(content['articles'])

# Access the article titles and Description
for article in content["articles"]:
    print(article['title'])
    print(article['description'])

