import requests
from bs4 import BeautifulSoup

r = open('./toonlinklist.txt', 'r')
ur = r.read()
url1=ur.split()
cn=0
urls = [
]
for u in url1:
    cn+=1
    urls.append(u)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

list = soup.select('div.content')
minus = soup.select('div.gallery.bbs div')
li = list[0].findAll('div')
cnt=2
while cnt > 1 and cnt<len(li)-3-len(minus) :
    a = li[cnt].findAll('a')
    for go in a:
        link = go['href']
        title = go.text
        print(link, title)
    cnt+=1
