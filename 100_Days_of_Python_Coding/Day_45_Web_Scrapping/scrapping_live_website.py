from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

article_tag = soup.find(name="tr", class_="athing")
article_text = article_tag.getText()

article_link = article_tag.find(name="a", class_="titlelink")


article_upvote = soup.find(name="span", class_="score")

print(article_text)
print(article_link.get("href"))
print(article_upvote.getText())