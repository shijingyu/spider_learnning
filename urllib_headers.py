# -*- coding: utf-8 -*-
# @Time    : 17-11-14 下午10:15
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : urllib_headers.py
# @Describe:
# @Software: PyCharm
import urllib,urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username':'cqc', 'password':'XXXX'}
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)

'''
另外，我们还有对付”反盗链”的方式，对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer

例如我们可以构建下面的headers
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
            'Referer':'http://www.zhihu.com/articles' }
1
2

headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
            'Referer':'http://www.zhihu.com/articles' }
'''
