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
# print(soup.title.string)


# changing whats inside the tag
# soup.title.string = "New Title"
# print(soup)

# find() & find_all()
# print(soup.find("p"))
# print(soup.find_all("p"))

# nested tags
table = soup.find("table")
table_tr = table.find_all("tr")[0]
print(table_tr.find_all("th"))
