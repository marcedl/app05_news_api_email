import requests

api_key = "d0b3301d6d00484698f336b19b927e27"
url = "https://newsapi.org/v2/everything?q=apple&from=2024-02-29&to=2024-02-29&sortBy=popularity&apiKey=d0b3301d6d00484698f336b19b927e27"

#Make a request 
request = requests.get(url)

#Got a dictionary with data
content = request.json()

#Access the data 
for article in content["articles"]:
    print(article["title"])
    print(article["description"])