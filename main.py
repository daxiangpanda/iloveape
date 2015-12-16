#!/usr/bin/env python
# encoding: utf-8

第一步：爬取搜索页面结果（http://www.loveape.com/t/music/q/%E7%BE%BD%E6%B3%89/count/20/cur/1/search.html）
http://www.loveape.com/t/music/q/%E7%BE%BD%E6%B3%89/count/20/cur/1/search.html
具体信息包括 歌曲名称 详情页url 专辑名称 歌手
第二步：通过详情页url爬取歌曲的songid sourceid 组成歌曲播放页面
在歌曲播放页面中，可以找到歌曲的具体地址
第三步：通过歌曲资源的地址下载歌曲到相应的文件夹

C:\Python27\python.exe -u C:\Program Files (x86)\JetBrains\PyCharm 4.5.4\helpers\pydev\pydevconsole.py 49554 49555
PyDev console: starting.

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\31351\\Documents\\GitHub\\interviewforprogrammers'])

Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
>>> url = 'http://www.loveape.com/ST/%E5%8D%8E%E8%AF%AD%E6%B5%81%E8%A1%8C/Q/%E7%BE%A4%E6%98%9F/%E6%88%91%E6%98%AF%E6%AD%8C%E6%89%8B%E7%AC%AC%E4%B8%80%E5%AD%A3%20-%E3%80%8A%E7%AC%AC9%E6%9C%9F%E3%80%8B[FLAC]/[%E6%9D%A5%E8%87%AA_www.loveape.com]%E7%BE%BD%E6%B3%89%20-%20%E7%94%B7%E4%BA%BA%E5%93%AD%E5%90%A7%E4%B8%8D%E6%98%AF%E7%BD%AA.mp3'
>>> import urllib2
>>> req = urllib2.Request(url)
>>> response = urllib2.urlopen(req)
>>> html = response.read()
>>> with open("E://音乐/男人哭吧不是罪.ape",'wb') as f:
...     f.write(html)
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'E://\xe9\x9f\xb3\xe4\xb9\x90/\xe7\x94\xb7\xe4\xba\xba\xe5\x93\xad\xe5\x90\xa7\xe4\xb8\x8d\xe6\x98\xaf\xe7\xbd\xaa.ape'
>>> with open(r"E:\音乐\男人哭吧不是罪.ape",'wb') as f:
...     f.write(html)
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'E:\\\xe9\x9f\xb3\xe4\xb9\x90\\\xe7\x94\xb7\xe4\xba\xba\xe5\x93\xad\xe5\x90\xa7\xe4\xb8\x8d\xe6\x98\xaf\xe7\xbd\xaa.ape'
>>> # encoding: utf-8
>>> with open(r"E:\音乐\男人哭吧不是罪.ape",'wb') as f:
...     f.write(html)
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'E:\\\xe9\x9f\xb3\xe4\xb9\x90\\\xe7\x94\xb7\xe4\xba\xba\xe5\x93\xad\xe5\x90\xa7\xe4\xb8\x8d\xe6\x98\xaf\xe7\xbd\xaa.ape'
>>> with open(r"E:\music\cry.ape",'wb') as f:
...     f.write(html)
...
>>> url = 'http://www.loveape.com/ST/%E5%8D%8E%E8%AF%AD%E6%B5%81%E8%A1%8C/Q/%E7%BE%A4%E6%98%9F/%E6%88%91%E6%98%AF%E6%AD%8C%E6%89%8B%E7%AC%AC%E4%B8%80%E5%AD%A3%20-%E3%80%8A%E7%AC%AC9%E6%9C%9F%E3%80%8B[FLAC]/[%E6%9D%A5%E8%87%AA_www.loveape.com]%E7%BE%BD%E6%B3%89%20-%20%E7%94%B7%E4%BA%BA%E5%93%AD%E5%90%A7%E4%B8%8D%E6%98%AF%E7%BD%AA.mp3'
>>> from urllib import urldecode
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ImportError: cannot import name urldecode
>>> from urllib import quote
>>> from urllib import dequote
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ImportError: cannot import name dequote
>>> from urllib import unquote
>>> unquote(url)
'http://www.loveape.com/ST/\xe5\x8d\x8e\xe8\xaf\xad\xe6\xb5\x81\xe8\xa1\x8c/Q/\xe7\xbe\xa4\xe6\x98\x9f/\xe6\x88\x91\xe6\x98\xaf\xe6\xad\x8c\xe6\x89\x8b\xe7\xac\xac\xe4\xb8\x80\xe5\xad\xa3 -\xe3\x80\x8a\xe7\xac\xac9\xe6\x9c\x9f\xe3\x80\x8b[FLAC]/[\xe6\x9d\xa5\xe8\x87\xaa_www.loveape.com]\xe7\xbe\xbd\xe6\xb3\x89 - \xe7\x94\xb7\xe4\xba\xba\xe5\x93\xad\xe5\x90\xa7\xe4\xb8\x8d\xe6\x98\xaf\xe7\xbd\xaa.mp3'
>>> for i in unquote(url).split("/"):
...     print i
...
http:

www.loveape.com
ST
华语流行
Q
群星
我是歌手第一季 -《第9期》[FLAC]
[来自_www.loveape.com]羽泉 - 男人哭吧不是罪.mp3
>>> print  unquote(url).split("/"):
...     pass
...
  File "<input>", line 1
    print  unquote(url).split("/"):
                                  ^
SyntaxError: invalid syntax
>>> print  unquote(url).split("/")
['http:', '', 'www.loveape.com', 'ST', '\xe5\x8d\x8e\xe8\xaf\xad\xe6\xb5\x81\xe8\xa1\x8c', 'Q', '\xe7\xbe\xa4\xe6\x98\x9f', '\xe6\x88\x91\xe6\x98\xaf\xe6\xad\x8c\xe6\x89\x8b\xe7\xac\xac\xe4\xb8\x80\xe5\xad\xa3 -\xe3\x80\x8a\xe7\xac\xac9\xe6\x9c\x9f\xe3\x80\x8b[FLAC]', '[\xe6\x9d\xa5\xe8\x87\xaa_www.loveape.com]\xe7\xbe\xbd\xe6\xb3\x89 - \xe7\x94\xb7\xe4\xba\xba\xe5\x93\xad\xe5\x90\xa7\xe4\xb8\x8d\xe6\x98\xaf\xe7\xbd\xaa.mp3']
>>> print  unquote(url)
http://www.loveape.com/ST/华语流行/Q/群星/我是歌手第一季 -《第9期》[FLAC]/[来自_www.loveape.com]羽泉 - 男人哭吧不是罪.mp3
>>> url = 'http://www.loveape.com/count/20/t/music/q/%E5%88%98%E5%BE%B7%E5%8D%8E/search.html'
>>> req = urllib2.Request(url)
>>> response = urllib2.urlopen(req)
>>> html = response.read()
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(html)
C:\Python27\lib\site-packages\bs4\__init__.py:166: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

To get rid of this warning, change this:

 BeautifulSoup([your markup])

to this:

 BeautifulSoup([your markup], "html.parser")

  markup_type=markup_type))
>>> soup = BeautifulSoup(html,"html.parser")
>>> soup.find_all("div",class_ = "pagebar")
[<div class="pagebar">\n<li class="dis" style=" width:54px;"><a>\u4e0a\u4e00\u9875</a></li><li class="cur"><a>1</a></li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/2/search.html">2</a></li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/3/search.html">3</a></li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/4/search.html">4</a></li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/5/search.html">5</a></li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/6/search.html">6</a></li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/7/search.html">7</a></li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/8/search.html">8</a></li><li style="color: #037C3D;">...</li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/11/search.html">11</a></li><li><a href="/t/music/q/\u5218\u5fb7\u534e/count/20/cur/2/search.html">\u4e0b\u4e00\u9875</a></li>\n</div>]
>>> len(soup.find_all("div",class_ = "pagebar"))
1
>>> soup.find_all("div",class_ = "pagebar")[0].children
<listiterator object at 0x000000000314F630>
>>> for i in soup.find_all("div",class_ = "pagebar")[0].children:
...     print i
...


<li class="dis" style=" width:54px;"><a>上一页</a></li>
<li class="cur"><a>1</a></li>
<li><a href="/t/music/q/刘德华/count/20/cur/2/search.html">2</a></li>
<li><a href="/t/music/q/刘德华/count/20/cur/3/search.html">3</a></li>
<li><a href="/t/music/q/刘德华/count/20/cur/4/search.html">4</a></li>
<li><a href="/t/music/q/刘德华/count/20/cur/5/search.html">5</a></li>
<li><a href="/t/music/q/刘德华/count/20/cur/6/search.html">6</a></li>
<li><a href="/t/music/q/刘德华/count/20/cur/7/search.html">7</a></li>
<li><a href="/t/music/q/刘德华/count/20/cur/8/search.html">8</a></li>
<li style="color: #037C3D;">...</li>
<li><a href="/t/music/q/刘德华/count/20/cur/11/search.html">11</a></li>
<li><a href="/t/music/q/刘德华/count/20/cur/2/search.html">下一页</a></li>


>>> for i in soup.find_all("div",class_ = "pagebar")[0].children:
...     print i.string
...


��һҳ
1
2
3
4
5
6
7
8
...
11
��һҳ


>>> max = 0
>>> for i in soup.find_all("div",class_ = "pagebar")[0].children:
...     if i.string.isdigit() and i.string>max:
...         max = i.string
...
>>> max
u'8'
>>> for i in soup.find_all("div",class_ = "pagebar")[0].children:
...     print i.string.isdigit()
...
False
False
True
True
True
True
True
True
True
True
False
True
False
False

