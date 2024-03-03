import requests
from send_email import send_email

topic = "tesla"
api_key = "d0b3301d6d00484698f336b19b927e27"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-02-03&sortBy=publishedAt&apiKey=d0b3301d6d00484698f336b19b927e27&language=en"

#Make a request 
request = requests.get(url)

#Got a dictionary with data
content = request.json()

#Access the data 
body = "Subject: Today's Tesla News" + "\n" 
for article in content["articles"][:20]:
    if (article["description"] is not None) & (article["title"] is not None):
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"
       
body = body.encode("utf-8")
send_email(body)