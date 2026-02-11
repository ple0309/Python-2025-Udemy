from bs4 import BeautifulSoup

import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# #Get part of tag using find()
# article_tag = soup.find(name="a", class_="storylink")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").text
# print(article_text)
# print(article_link)
# print(article_upvote)
#################################################################################
#Get list not part of it using find_all().
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

#using split()[0] to split '40 points' into two parts and take first one for number only.
# turn it into integer.
article_upvotes = [int(score.text.split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])







###############################################################################
#### Lesson
# import lxml
#
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title) #will return <title>Angela's Personal Site</title>
# # print(soup.title.name) #will return title
# # print(soup.title.string) #will return Angela's Personal Site
# #
# #
# # print(soup) #print everything inside html file
# # print(soup.prettify()) #also print everything inside html file but with reasonable indent.
# # print(soup.a)  #first anchor tag.
# # print(soup.li) #first li.
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText()) #will print out the text inside tag name a.
#     print(tag.get("href"))
#
# #print following the id inside h1.
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# #print following the class inside h3
# section_heading = soup.find(name="h3", class_ ="heading")
# print(section_heading)
# print(section_heading.get("class")) #return the name of class inside section_heading
#
# #####################################################################
# #Select_one based on style css selector p > a to get children inside p.
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# #To select the id = name, it should have the # sign in it.
# name = company_url = soup.select_one(selector="#name")
# print(name)
#
# #To select the class of all heading class then put them into a list.
# headings = soup.select(".heading")
# print(headings)