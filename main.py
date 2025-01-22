import requests

api_key = "fa2381d645ab46ad939989f041aca363"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=fa2381d645ab46ad939989f041aca363"

#make request
request = requests.get(url)

#get a dictionary with data
content = request.json()

#access thhe article titles and description
for article in (content["articles"]):
    print(article["title"])
    print(article["description"])
