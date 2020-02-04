import requests 
from bs4 import BeautifulSoup

#using requests module we use the 'get' function to access the webpage provided
result = requests.get("https://www.google.com/")
#We check the status code to see if we get hte 200 (OK) response
print(result.status_code)
#header data
#print(result.headers)

#The content of the page
src = result.content
#print(src)

#beautiful soup allows us to take all that junk and parse and process into something useful
soup  = BeautifulSoup(src)

#lets look at links on page - "a" refers to a tag which is a link
links = soup.find_all("a")
print(links)
print("\n")

#if we want just the links that contaisn the text "About", we can use the built in text function to access the text content between the <a></a> tags
for link in links:
    if "About" in link.text:
        print(link)
        #insdie the <a> tag there is an attribute called href
        print(link.attrs['href'])

