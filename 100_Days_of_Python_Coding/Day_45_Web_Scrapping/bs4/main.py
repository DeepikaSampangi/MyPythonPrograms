import lxml
from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_a_tags = soup.find_all(name="a")

for tag in all_a_tags:
    print(tag.getText())
    print(tag.get("href"))

company_url = soup.select_one(selector="p a")
print(company_url)
