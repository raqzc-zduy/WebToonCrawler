from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime

# r = open('./marutoonlinklist.txt', 'r')
r2 = open('./lezhintoonlist01.txt', 'r')
now = datetime.now()
t = open('./lezhintoonlist01.txt', 'w', encoding='utf-8')

url = 'https://www.lezhin.com/ko/comic/devildom'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

imglist = soup.select('div.banner-wrap')
img = imglist[0].find('img')['src']
print(img)

authorlist = soup.select('div.info')
author = authorlist[0].find('p').find('a').text
print(author)

list = soup.select('section.episode-main')
print(list)
print(len(list))

r2.close()
t.close()