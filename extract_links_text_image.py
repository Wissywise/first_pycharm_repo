import requests # import the requests library to send HTTP requests
from bs4 import BeautifulSoup # import the BeautifulSoup library to parse HTML content

url = "https://books.toscrape.com/"
print("Stepping into the world of web scraping with Python! Today, we're going to scrape some data from a website and extract useful information. Let's get started!\n")
print("First, we need to send a request to the website to get the HTML content. We'll use the requests library for this. \n")
print("Sending a GET request to the URL: \n", url )
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser') # now we have the HTML content, we can use BeautifulSoup to parse it and extract the information we need.
print("Now that we have the HTML content, we can use BeautifulSoup to parse it and extract the information we need. \n")

print("Let's start by extracting all the links from the page. We'll look for all the 'a' tags and get their 'href' attributes. \n")

titles = soup.find_all('h3') # find all the h3 tags, which contain the titles of the books
for title in titles:
    link = title.find('a')['href'] # get the href attribute of the a tag inside the h3 tag
    print("Book Title: ", title.text.strip()) # print the text of the h3 tag, which is the title of the book
    print("Link: ", url + link) # print the full URL of the book by concatenating the base URL with the href attribute
    print("\n")

links = soup.find_all('a') # find all the a tags, which contain the links
for link in links:
    href = link.get('href') # get the href attribute of the a tag
    if href: # check if the href attribute is not None
        print("Link: ", url + href) # print the full URL of the link by concatenating the base URL with the href attribute
        print("\n")

"""images = soup.find_all('img') # find all the img tags, which contain the images
for image in images:
    src = image.get('src') # get the src attribute of the img tag
    if src: # check if the src attribute is not None
        print("Image: ", url + src) # print the full URL of the image by concatenating the base URL with the src attribute
        print("\n")"""

images = soup.find_all('img') # find all the img tags, which contain the images
for image in images:
    print("http://books.toscrape.com/" + image['src'].replace("../", "")) # print the full URL of the image by concatenating the base URL with the src attribute
