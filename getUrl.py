import requests
from bs4 import BeautifulSoup
import base64


def getUrl(language, key, items):
    categories = ["science-topics-20", "technology-topics-102", "india-topics-15", "automobile-topics-101", "entertainment-topics-8", "sports-topics-17", "world-topics-16", "lifestyle-topics-11", "employment-topics-136", "religion+spirituality-topics-135", "football-topics-495", "movie+review-topics-807"]

    languages = ["english", "hindi", "marathi", "gujarati", "punjabi", "bangla", "kannada", "tamil", "telugu", "malayalam", "oriya", "urdu", "bhojpuri", "nepali"]

    categoryDict = {
        'science': categories[0],
        'technology': categories[1],
        'india': categories[2],
        'automobile': categories[3],
        'entertainment': categories[4],
        'sports': categories[5],
        'world': categories[6],
        'lifestyle': categories[7],
        'employment': categories[8],
        'religion': categories[9],
        'football': categories[10],
        'movie': categories[11]
    }
    
    if(language == None):
        language = languages[0]

    category = categoryDict[key]
    base_url = f"https://m.dailyhunt.in/news/india/{language}/{category}"
    soup = BeautifulSoup(requests.get(base_url).content, "lxml")
    encodedUrl = soup.find("input").get("value")
    url = base64.b64decode(encodedUrl).decode('utf-8')
    if(items != None):
        try:
            url = url.replace('pageSize=10', f'pageSize={items}')
        except:
            return "<h1>items can only be in whole-numbers</h1>"

    return url