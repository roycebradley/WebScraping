import requests 
from bs4 import BeautifulSoup

#Goal is to get all links from whitehouse briefings
#and statements page.
#

result = requests.get("https://www.whitehouse.gov/briefings-statements/")

src = result.content

#create the soup object
soup = BeautifulSoup(src)

urls = []

for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find("a")
    urls.append(a_tag.attrs['href'])

print(urls)
