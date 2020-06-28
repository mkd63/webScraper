from bs4 import BeautifulSoup
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content,"html.parser")

print(content.prettify())
def parse(url):
    headers = {'User-Agent':'Chrome/47.0.2526.106'}
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.content, 'lxml')
    #text = '\n'.join([i.text for i in soup.select('.description p')])
    #tweet = soup.findAll('p', attrs={"class": "content"})
    #tweetText= tweet.get_text()
    #for tweet in soup.find_all('p', attrs={"class": "content"}):


    tweetArr = []
    for tweet in soup.findAll('div', attrs={"class": "tweetcontainer"}):
        tweetObject = {
            "author": tweet.find('h2', attrs={"class": "author"}).text,
            "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
            "tweet": tweet.find('p', attrs={"class": "content"}).text,
            "likes": tweet.find('p', attrs={"class": "likes"}).text,
            "shares": tweet.find('p', attrs={"class": "shares"}).text
        }
        tweetArr.append(tweetObject)
    with open('twitterData.json', 'w') as outfile:
        json.dump(tweetArr, outfile)
    return tweetArr

parse('http://ethans_fake_twitter_site.surge.sh/')
tweet = content.findAll('p', attrs={"class": "content"})
