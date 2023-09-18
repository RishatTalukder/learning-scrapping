# importing beautifulsoup4
from bs4 import BeautifulSoup

# opening the html file
with open("dummy.html", "r") as f:
    # parsing the html file
    soup = BeautifulSoup(f, "html.parser")

# to make the output prettier
# print(soup.prettify())

# printing the h1 tag
# print(soup.h1)

# printing the title
# print(soup.title)

# printing the string inside the title tag
#print(soup.title.string)


#changing whats inside the tag
# soup.title.string = "New Title"
# print(soup)

