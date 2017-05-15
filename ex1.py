import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()
# file_path = datetime.strftime(now, "./scrap_%Y-%m-%d_%H:%M:%S.txt")
# file_path = datetime.strftime(now, "./%Y-%m-%d_%H:%M.txt")
# file_path = datetime.strftime(now, "./%H_%M_%S.txt")
# f = open(file_path, 'w', encoding='utf-8')
# toonlist = open('./toonlist.txt', 'w', encoding='utf-8')
url = 'http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
list = soup.select('table tr')
cnt=1
for li in list:
    if url != "http://comic.naver.com/webtoon/list.nhn?titleId=25455&weekday=tue" and url != 'http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue':
        if cnt < 3:
            cnt = cnt + 1
            continue
        li2 = li.find('img')['src']
        title = li.find_all('a')
        href = title[1]['href']
        date = li.find_all('td')
        print(li2, title[1].text, 'http://comic.naver.com' + href, date[3].text)
    else:
        if cnt < 4:
            cnt = cnt + 1
            continue
        li2 = li.find('img')['src']
        title = li.find_all('a')
        href = title[1]['href']
        date = li.find_all('td')
        print(li2, title[1].text, 'http://comic.naver.com' + href, date[3].text)