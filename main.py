import requests
from send_email import send_email

api_key = "d0b3301d6d00484698f336b19b927e27"
url = "https://newsapi.org/v2/everything?q=apple&from=2024-02-29&to=2024-02-29&sortBy=popularity&apiKey=d0b3301d6d00484698f336b19b927e27"

#Make a request 
request = requests.get(url)

#Got a dictionary with data
content = request.json()

#Access the data 
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"
       
body = body.encode("utf-8")
send_email(body)