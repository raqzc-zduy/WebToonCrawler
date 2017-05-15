import requests
import urllib
from bs4 import  BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

urls = [
'http://comic.naver.com/webtoon/weekday.nhn'
]
class MainParser:
    def __init__(self, func=None):
        if func:
            self.parse_url = func

    def parse_url(self, _url):
        print("미구현")
        print(_url)

def naver_parser(_url):
    response = requests.get(_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    list = soup.select('div.col_inner ul li')
    cnt = 1
    data = ''
    tlist = ''
    for li in list:
        li2 = li.find_all('a')
        thumb = li.find('div').find('a').find('img')['src']
        print(cnt, thumb, li2[1].text, 'http://comic.naver.com' + li2[1]['href'])
        data += "[%3d번째 웹툰] 썸네일주소 : %s, 웹툰명 : %s, 웹툰주소 : %s\n" % \
                (cnt, thumb, li2[1].text, 'http://comic.naver.com' + li2[1]['href'])
        tlist += "%s\n" % ("http://comic.naver.com" + li2[1]['href'])
        cnt = cnt + 1

    return data

parser_select_dict = {
    'comic.naver.com': naver_parser
}

now = datetime.now()
file_path = datetime.strftime(now, "./%H_%M_%S.txt")

def scraping():
    data = ''
    f = open(file_path, 'w', encoding='utf-8')
    for url in urls:
        parsed_url = urlparse(url)
        print(parsed_url[1])
        func = parser_select_dict[parsed_url[1]]
        parser = MainParser(func)
        f.write(parser.parse_url(url))
        print(parser.parse_url(url))
    f.close()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    print("START")
    scheduler.add_job(scraping, 'interval', seconds=10)

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        print("EXIT")
        pass







