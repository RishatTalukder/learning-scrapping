# Lets Learn Web-Scraping with Python

I had no idea how or where to start. So, I started finding tutorials on Youtube and i found this one.

- <a href="https://www.youtube.com/watch?v=7b3j1uNcF6E">Web Scraping with Python</a>

### So, What is Web Scraping?

web scraping is the process of extracting data from a website.

thats it. Simple...

### BUT HOW!!

### How to do Web Scraping?

there are several ways to do it.

1. Beautiful Soup
2. Selenium
3. Scrapy

#### The easiest would be <i>Beautiful Soup</i>.

#### !!!-- lets start --!!!

# Installation

- pip install beautifulsoup4

Install the module from the command line.

You can use any code editor to write your code. Im using Vs Code.

So, Start by making a new file.

I named my file <code>web_scraping.py</code>

- first we need to import the module.

```python
from bs4 import BeautifulSoup
```

Now, we need a website to scrape. so, i will make a simple dummy html page.

i'll name it <code>dummy.html</code>

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Dummy HTML Page</title>
  </head>
  <body>
    <h1>Welcome to Dummy HTML Page</h1>

    <p>This is a paragraph.</p>

    <h2>List of Fruits</h2>
    <ul>
      <li>Apple</li>
      <li>Orange</li>
      <li>Banana</li>
    </ul>

    <h3>Table of Users</h3>
    <table>
      <tr>
        <th>Name</th>
        <th>Age</th>
      </tr>
      <tr>
        <td>John</td>
        <td>25</td>
      </tr>
      <tr>
        <td>Jane</td>
        <td>30</td>
      </tr>
    </table>

    <div>
      <h4>Important Message</h4>
      <p>This is an important message within a div element.</p>
    </div>

    <footer>
      <p>&copy; 2022 Dummy HTML Page. All rights reserved.</p>
    </footer>
  </body>
</html>
```

as you can see its a small html page with some nested tags and some different type of html elements.

now to scrape this page we need to open the file with python and read it.

```python
with open('dummy.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')
```

Now we break it down step by step:

- `with open('dummy.html', 'r') as f:` opens the dummy.html file, with the 'r' mode, meaning we can only read the file but not write to it.

- `soup = BeautifulSoup(f, 'html.parser')` creates a variable called <code>soup</code> and assigns it to the <code>BeautifulSoup</code> class, in which the file <code>dummy.html</code> is passed as an argument.

- and dont forget to indent after `with open('dummy.html', 'r') as f:`

Now if we do `print(soup)` you will see some gibberish. That is not readable. SO, to make it more readable we need to use the <code>prettify()</code> method.

```python
print(soup.prettify())
```

Now, after running the python file, you get something similler to the dummy html page.

# Finding a tag

## "." Operator

In general, the simplest way to find a tag would be to use the <code>"."</code> operator.

```python
print(soup.h1)
```

Here we are instructing python to print the <code>h1</code> tag from the <code>soup</code> variable.

run the code and you will see whats inside the first <code>h1</code> tag.

you can also try,

```python
print(soup.title)
```

But there is an issue. In the output you might see Something like this:

> `<title>Dummy HTML Page</title>`

We need the data inside the tag not the tag itself. So, we need to use the <code>"."</code> operator again.

```python
print(soup.title.string)
```

Now you will see the data inside the tag.

> `Dummy HTML Page`

Here, soup.title<code>.string</code></code> is used which returns the data inside the tag.

You can also change whats inside the tag.

just add these lines of code.

```python
soup.title.string = 'New Title'
print(soup.prettify())
```

> Now if you look for the title tag again, you will see the new title.

## Find() & Find_all()

Before starting we should clean up the code and keep these part.

```python
# importing beautifulsoup4
from bs4 import BeautifulSoup

# opening the html file
with open("dummy.html", "r") as f:
    # parsing the html file
    soup = BeautifulSoup(f, "html.parser")
```

So, `find()` and `find_all()` are used to find a tag.But find() returns only the first tag and find_all() returns all the tags.

```python
print(soup.find("p"))
print(soup.find_all("p"))
```

The output will be,

- For `find()`:

> `<p>This is a paragraph.</p>`

- for `find_all()`:

> `[<p>This is a paragraph.</p>, <p>This is an important message within a div element.</p>, <p>© 2022 Dummy HTML Page. All rights reserved.</p>]`

> Must try it yourself

As, you can see the output for `find()` id just the first <code>p</code> tag. But for `find_all()` it returns an list of all the <code>p</code> tags.

### Finding data from Nested Tags

Now, If you have abother look at the dummy.html file, you will see that there is a nested tag.

```html
<table>
  <tr>
    <th>Name</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>John</td>
    <td>25</td>
  </tr>
  <tr>
    <td>Jane</td>
    <td>30</td>
  </tr>
</table>
```

Lets get the Table data.

```python
print(soup.find("table"))
```

> i used the <code>find()</code> method because there is only one `table` tag.

you will see the the above html table printed out.

Now we need to extract the data, so, we will start by getting the nested `tr` tag.

> remove the `print(soup.find("table"))` and write

```python
table = soup.find("table")
print(table.find_all("tr"))
```

> im using `find_all()` because there are multiple `tr` tags.

after running the code you will see all the `tr` tags inside the `table` tag listed.

You can now use the Same method to find the data from `td` or `th` tags. Try to do it yourself.

-if your struggling to figure it out.

```python
...
print(table.find_all("td"))
print(table.find_all("th"))
```

This will give you all the <code>td</code> and <code>th</code> tags.

but to find a specific data inside a tag you should use this method.

```python
table_tr = table.find_all("tr")[0]
print(table_tr.find_all("th"))
```

this will give you the <code>th</code> tags inside the first <code>tr</code> tag.

I hope you got the gist of Beautiful Soup 4.

!!!-- NOOOOOOOOOWWWW --!!!

#### lets use it to scrape a website

# Scraping a live website

## Installation

- Make a new python file. i will name it <code>scraping.py</code>
- pip install requests
- pip install beautifulsoup4

now we can start writting.

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```