import requests
from bs4 import BeautifulSoup

url='https://www.google.com/search?q=Python'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
headings = soup('h3')
for heading in headings:
    print(heading.find('div').text)
