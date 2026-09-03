import requests
from bs4 import BeautifulSoup

# Step 1: Set the target URL
url = "https://books.toscrape.com/"
print("Step 1: URL is set.\n")

# Step 2: Send a GET request to the website
response = requests.get(url)
print("Step 2: GET request sent successfully.\n")

# Step 3: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")
print("Step 3: HTML content parsed using BeautifulSoup.\n")

# Step 4: Extract all book titles
print("Step 4: Extracting Book Titles:\n")
titles = soup.find_all("h3")
for title in titles:
    print(title.a["title"])
print("\nStep 4 Completed: All book titles extracted.\n")

# Step 5: Extract all links
print("Step 5: Extracting Links:\n")
links = soup.find_all("a")
for link in links:
    href = link.get("href")
    if href:
        print(href)
print("\nStep 5 Completed: All links extracted.\n")

# Step 6: Extract all image sources
print("Step 6: Extracting Image URLs:\n")
images = soup.find_all("img")
for img in images:
    print("https://books.toscrape.com/" + img["src"].replace("../", ""))
print("\nStep 6 Completed: All image URLs extracted.\n")
