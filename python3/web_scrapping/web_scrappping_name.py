import requests
from bs4 import BeautifulSoup

# url containing top 100 baby names
url = "https://www.babycenter.com/baby-names/most-popular/top-baby-names-2024"

response = requests.get(url)

# print(response.content)

# Assuming `html_doc` contains your HTML document
soup = BeautifulSoup(response.content, 'html.parser')

# Find all `<a>` tags
links = soup.find_all('a')

# Extract 'href' attribute from each link
for link in links:
    print(link.get('href'))