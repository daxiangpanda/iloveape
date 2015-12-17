#!/usr/bin/env python
# encoding: utf-8
import urllib2
from bs4 import BeautifulSoup

#oepn url
def url_open(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html,'html.parser')
    return soup


#获取搜索页面的数量
def get_page(url):
    soup = url_open(url)
    max = 0
    for i in soup.find_all("div",class_ = "pagebar")[0].children:
        print i
        if i.string.isdigit() and i.string>max:
            max = int(i.string)
    return max


def get_info(url):
    soup = url_open(url)
    tag = soup.find_all("tr",class_ = "song")
    # name = soup.find_all("a",class_ = "name")
    # url =
    # album =
    # singer =
    # info = [name,url,album,singer]
    output = []
    # print tag
    for i in tag:
        suboutput = []
        # print i
        n = 0
        for ii in i.children:

            # if n == 0:
            #     n = n+1
            #     continue
            # elif n == 1:
            #     for iii in ii.children:
            #         name_song = iii.string
            #         url_song = iii.get("href")
            #         print name_song
            #         print url_song
            #     n = n+1
            # elif n == 2 :
            #     for iii in ii.children:
            #         name_cd = iii.string
            #         url_cd = iii.get("href")
            #         print name_cd
            #         print url_cd
            #     n = n+2
            # elif n == 5:
            #     for iii in ii.children:
            #         name_singer = iii.string
            #         print name_singer
            #     n+=2
            print '/////'
            print ii
            print '/////////////'
    return tag
url = 'http://www.loveape.com/t/music/q/%E5%88%98%E5%BE%B7%E5%8D%8E/count/20/cur/1/search.html'
get_info(url)

