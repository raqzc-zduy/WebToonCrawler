import requests
from bs4 import BeautifulSoup

url = 'http://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon&page='

number = 0
stop = 1
list2 = None

while stop == 1:
    number += 1
    response = requests.get(url + str(number))
    soup = BeautifulSoup(response.text, 'html.parser')
    list = soup.select('table tr')

    if list != list2:
        nexturl = 'http://comic.naver.com/'
        for li in list:
            if li != list[0] and li != list[1]:
                a = li.find('a')
                link = a['href']
                img = a.find('img')['src']
                title = a.find('img')['title']
                print(nexturl + link)
                print(img)
                print(title)
    else:
        break
    list2 = list
    print('------------------------------------------------------------------' + str(number) + '-----------------------------------------------------------------------------')
    print()