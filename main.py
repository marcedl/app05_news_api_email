import requests

api_key = "d0b3301d6d00484698f336b19b927e27"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d0b3301d6d00484698f336b19b927e27"

request = requests.get(url)
content = request.json()
print(content["articles"])