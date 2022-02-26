from bs4 import BeautifulSoup
import requests


response=requests.get(url="https://news.ycombinator.com/")
data=response.text

soup=BeautifulSoup(data, "html.parser")

articles=soup.find_all(class_="titlelink")
article_texts=[]
article_links=[]

#fetches all the article's titles and links
for article_tag in articles:
    article_texts.append(article_tag.get_text())
    article_links.append(article_tag.get("href"))

#fetches the number of upvotes of each article
article_upvotes_tags =soup.find_all(class_="score")
article_upvotes=[int(score.get_text().split()[0]) for score in article_upvotes_tags ]

#gets the article with the most upvotes and shows the title, link and number of upvotes
max_upvote=max(article_upvotes)
index=article_upvotes.index(max_upvote)
max_title=article_texts[index]
max_link=article_links[index]

print(f"{max_title}\n{max_link}\n{max_upvote}")

