import requests
from send_email import send_email_m

# topic you want to search
topic = "tesla"

# get api key and url from newsapi.org
api_key = '793b70fa6a734a30aab62307ede9b395'
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2022-10-22&" \
      "sortBy=publishedAt&apiKey=793b70fa6a734a30aab62307ede9b395&" \
      "language=en"

request = requests.get(url)
# convert string into dict to extract info
content = request.json()

# string for email parameter
body = ""
# Access the article titles and Description and store in body
# Set to a min of 20 articles
for article in content["articles"][:20]:
    if article['title'] is not None:
        body = "Subject: Top US business Headlines" + \
               "\n" + body + article['title'] + '\n' + \
               article['description'] + '\n' + article['url'] + 2*"\n"
body = body.encode('utf-8')
send_email_m(message=body)


