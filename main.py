#!/usr/bin/env python
# encoding=utf-8
import urllib2
from bs4 import BeautifulSoup
from urllib import unquote
from urllib import quote
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
        # print i
        n = 0
        suboutput = []
        for ii in i.children:
            # print '////'
            # print ii
            k = n%8
            # pass
            if k == 0:
                n+=1
            elif k == 1:
                for iii in ii.children:
                    name_song = iii.string
                    url_song = iii.get("href")
                    # print u'歌曲名：'+name_song
                    # print url_song
                    suboutput.append(name_song)
                    # print suboutput[0]
                    suboutput.append(url_song)
                    # print suboutput
                n+=1
            elif k == 2:
                n+=1
            elif k == 3:
                for iii in ii.children:
                    name_cd = iii.string
                    url_cd = iii.get("href")
                    # print u'专辑：'+name_cd
                    # print url_cd
                    suboutput.append(name_cd)

                    suboutput.append(url_cd)
                    # print suboutput
                n+=1
            elif k == 4:
                n+=1
            elif k == 5:
                for iii in ii.children:
                    name_singer = iii.string
                    suboutput.append(name_singer)
                    # print suboutput
                    # print u'歌手：'+name_singer
                n+=1
            elif k == 6:
                n+=1
            elif k == 7:
                song_id = ii.find_all("li",class_ = "play-icon entry")[0].get("data-music")
                source_id = ii.find_all("li",class_ = "play-icon entry")[0].get("data-sourceid")
                # print u'歌曲ID：'+song_id
                # print u'资源ID：'+source_id
                suboutput.append(song_id)
                suboutput.append(source_id)
                # print suboutput
                n+=1
            elif k == 8:
                n+=1
                # print suboutput
                # print '\n'
        output.append(suboutput)
    # for i in output:
    #     for ii in i:
    #         print ii
    return output


def get_source(url):
    soup = url_open(url)
    return 'http://www.loveape.com'+soup.find_all("tr")[1].get("data-src")
#   print


def process_output(output):
    processed = []
    url_root = u'http://www.loveape.com/'
    for i in output:
        dict = {}
        dict['name_song'] = i[0]
        dict['name_cd'] = i[2]
        # http://www.loveape.com/t/add/songID/117233/sourceid/20150507397511/ListenMusic.html
        dict['url_song'] = url_root+'t/add/songID/'+i[5]+'/sourceid/'+i[6]+'/ListenMusic.html'
        # print dict['url_song']
        dict['url_resource'] = get_source(dict['url_song'])
        print dict
        processed.append(dict)
    return processed


def download(url):
    pass

url = 'http://www.loveape.com/t/music/q/%E5%88%98%E5%BE%B7%E5%8D%8E/count/20/cur/1/search.html'
url_song = 'http://www.loveape.com/t/add/songID/28005/sourceid/20141107589657/ListenMusic.html'
print get_info(url)
print process_output(get_info(url))



