import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(response.text, "html.parser")

article_texts = []
article_links = []
articles = soup.find_all(name="tr", class_="athing")
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.find(name="a", class_="titlelink").get("href"))

article_upvotes = [
    int((score.getText()).split(" ")[0])
    for score in soup.find_all(name="span", class_="score")
]

print(article_texts)
print(article_links)
print(article_upvotes)

max_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])
