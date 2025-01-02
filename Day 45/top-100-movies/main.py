from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
raw_data = response.text

soup = BeautifulSoup(raw_data, "html.parser")
descriptions = soup.findAll("p", class_="description")

directors = []
textss = []


for article_tag in descriptions:
    text = article_tag.getText()
    textss.append(text)
    link = article_tag.find(name='a').get(soup.a.text)
    directors.append(link)

print(directors)
print(textss)


# titles = soup.findAll("h3", class_="title")
#
# title_texts = []
#
# for title_tag in titles:
#     text = title_tag.getText()
#     title_texts.append(text)
#
# with open('text.txt', 'w+') as f:
#     # write elements of list
#     for items in title_texts:
#         f.write('%s\n' % items)
#
#     print("File written successfully")
#
# # close the file
# f.close()
#
