

from bs4 import BeautifulSoup
import requests
print("hello")

url = "https://www.wsj.com/search/term.html?KEYWORDS=coronavirus&mod=searchresults_viewallresults"
r1 = requests.get(url)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all('h3', class='headline')

print(coverpage_news[0])