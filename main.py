import requests
from send_email import send_email

api_key = "fa2381d645ab46ad939989f041aca363"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=fa2381d645ab46ad939989f041aca363"

#make request
request = requests.get(url)

#get a dictionary with data
content = request.json()

#access thhe article titles and description
body = ""
for article in (content["articles"]):
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"


body = body.encode("utf-8")
send_email(message=body)

