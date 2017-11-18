# -*- coding: utf-8 -*-
# @Time    : 17-11-15 下午8:57
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : qiushibaike.py
# @Describe:
# @Software: PyCharm
import re
import urllib, urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>',re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item[0],item[1],item[2]
        #item[1],item[2],item[3]
       # print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
