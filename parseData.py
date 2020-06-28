import json

with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

for i in jsonData:
    print("Author: " + i['author'])
    print("Date: " + i['date'])
    print("Tweet: " + i['tweet'])
    print("Likes: " + i['likes'])
    print("Shares: " + i['shares'])
