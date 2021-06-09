from getUrl import getUrl
import requests
import json
from bs4 import BeautifulSoup


def paraParse(newsContent):
    soup = BeautifulSoup(newsContent, "lxml")
    pTags = soup.findAll("p")
    content = ""
    for i in range(len(pTags)):
        content = content + pTags[i].text + "\n"
    return content.strip()


def getNews(language, category, items):
    url = getUrl(language, category, items)

    responseDict = json.loads(requests.get(url).content)
    rows = responseDict["data"]["rows"]

    count = responseDict['data']['count']

    newsDictionary = {
        'success': True,
        'category': category,
        'count': count,
        'data': []
    }

    for row in rows:
        try:
            title = row["title"]
        except:
            title = ""
        try:
            url = row["shareUrl"]
        except:
            url = ""
        try:
            contentImage = row["contentImage"]
        except:
            contentImage = ""
        try:
            ImageUrl = contentImage["url"]
        except:
            ImageUrl = ""
        try:
            counter = row["counter"]
        except:
            counter = ""
        try:
            PublishedDt = counter["ingestionDate"]
        except:
            PublishedDt = ""
        try:
            viewCount = counter["viewsCount"]
        except:
            viewCount = ""
        try:
            newsContent = row["content"]
            content = paraParse(newsContent)
        except:
            content = ""
        try:
            publisherStory = row["publisherStoryUrl"]
        except:
            publisherStory = ""

        newsObject = {
            'title': title,
            'imageUrl': ImageUrl,
            'url': url,
            'content': content,
            'PublishedTime': PublishedDt,
            'viewCount': viewCount,
            'publisherStory': publisherStory
        }

        newsDictionary['data'].append(newsObject)

    return newsDictionary
