#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import random

def find_content(f, url):
    res = requests.get(url)
    res.encoding = 'GB18030'
    soup = BeautifulSoup(res.text.replace('&nbsp;', ' '), 'html.parser')
    title = soup.select('.bookname h1')[0].text
    print(title)
    tt = soup.select('#content')[0].text
    f.write(title + '\n\n' + tt + '\n\n')

if __name__ == "__main__":

    url = 'http://www.biquge.com.tw/2_2016/'  # 小说目录页的网址
    url1 = 'http://www.biquge.com.tw/'
    headers = {'Host': 'www.biquge.com.tw',
               'Connection': 'keep-alive',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    IPs = [
        {'HTTPS': 'https://115.237.16.200:8118'},
        {'HTTPS': 'https://42.49.119.10:8118'},
        {'HTTPS': 'http://60.174.74.40:8118'}
    ]
    IP = random.choice(IPs)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    #创建Beautiful Soup对象
    mulu = soup.find_all('dd')
    sub_lst = []
    with open('遮天.txt', 'a+',encoding='gb18030') as f:
        for link in mulu:
            sub_url = url1 + link.find('a').get('href')
            sub_lst.append(sub_url)
            find_content(f, sub_url)
