# DailyHunt API

This API is capable of fetching news contents from various sources as gathered by DailyHunt.

---

## News Categories

This API supports category wise news. Here is a complete list of all categories.

1. Science
2. Technology
3. India
4. automobile
5. entertainment
6. sports
7. world
8. lifestyle
9. employment
10. religion
11. football
12. movie

---

## Usage

---
see all the available categories
```
https://dailyhunt.vandit.cf/categories
```
Example - https://dailyhunt.vandit.cf/categories

---
see all the available languages
```
https://dailyhunt.vandit.cf/languages
```
Example - https://dailyhunt.vandit.cf/languages

---
Make a request specifying the category of news you want
```
https://dailyhunt.vandit.cf/dailyhunt?category=<your-category>
```
Example - https://dailyhunt.vandit.cf/dailyhunt?category=technology

---
Make a request specifying the language of news you want
```
https://dailyhunt.vandit.cf/dailyhunt?category=<your-category>&language=<your-language>
```
Example - https://dailyhunt.vandit.cf/dailyhunt?category=technology&lang=hindi

---
Make a request specifying items you want in on page
```
https://dailyhunt.vandit.cf/dailyhunt?category=<your-category>&items=<your-items>
```
Example - https://dailyhunt.vandit.cf/dailyhunt?category=technology&lang=hindi&items=30

---

## Parameters

- Optional Parameters
    - Language
    - Items

- Compulsory Parameters
    - Category

### Default values of the parameters:

    - Language = english
    - items = 10

---

## Response Format

The response JSON Object looks something like this - 

```
{
  category: "world",
  count: 10,
  data: [
  { 
    PublishedTime: "2021-06-09 09:08:32",
    content: "Damascus [Syria], June 9 (ANI): A fresh Israeli missiles strike targeted military sites in Syria on Tuesday night, Syrian media reported. The Syrian army said it shot down some missiles fired by Israel, Syria's state news agency SANA reported The Syrian air defences were triggered by the attack as people in the capital of Damascus saw Syrian air defence missiles being fired into the sky.SANA said the Israeli attack was launched from inside the Lebanese airspace, as Israeli warplanes usually attack Syria from Lebanon.Some people in the northwestern province of Latakia and the central province of Homs told Xinhua that they also witnessed an Israel i attack.",
    imageUrl: "http://assets-news-bcdn.dailyhunt.in/cmd/resize/400x400_80/fetchdata16/images/90/31/ee/9031ee1a88a2295db9640fd2d0d0b09efc41829f5bb1657f448321b004016b22.jpg",
    publisherStory: "https://www.aninews.in/news/world/middle-east/destroyed-missiles-fired-by-israel-says-syria20210609053541",
    title: "Destroyed missiles fired by Israel, says Syria",
    url: "http://dhunt.in/gYtlp",
    viewCount: "667"
  },
  {
    PublishedTime: "2021-06-09 09:08:32",
    content: "Washington [US], June 9 (ANI): US Senate on Tuesday passed bipartisan legislation aimed at countering China's growing influence by investing over USD 200 billion in American technology, science and research. The final vote was 68-32. Independent Senator Bernie Sanders of Vermont was the only member of the Democratic caucus to vote against the bill. Nineteen Senate Republicans joined Democrats voting in favour of the bill, CNN reported. The bill still needs to pass the House before going to President Joe Biden's desk. The sweeping legislation -- called the US Innovation and Competition Act -- aims to confront China 's influence on multiple fronts and "will supercharge American innovation and preserve our competitive edge for generations to come," said Majority Leader Chuck Schumer who co-wrote the bill. Schumer described the vote as a necessary step to keep America in the game against countries such as China , and a significant legislative accomplishment after months of behind-the-scenes talks.",
    imageUrl: "http://assets-news-bcdn.dailyhunt.in/cmd/resize/400x400_80/fetchdata16/images/31/35/3d/31353d4a7e3353606d2b81bc5258618986b6b5306b84babba81dd579b7ae9491.jpg",
    publisherStory: "https://www.aninews.in/news/world/us/us-senate-passes-bipartisan-bill-to-counter-chinas-growing-economic-influence20210609051334",
    title: "US Senate passes bipartisan bill to counter China's growing economic influence",
    url: "http://dhunt.in/gYlT2",
    viewCount: "5.1k"
  },
],
  "success": true
}
```
---
## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```
---

### You can fork the repo and deploy on VPS, Heroku or Vercel :)
[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/vendz/inshorts-api/tree/main)

---
#### :star: the Repo in case you liked it :)
#### Made with :heart: in India

# © [Vandit](https://github.com/vendz)
