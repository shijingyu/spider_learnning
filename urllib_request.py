# -*- coding: utf-8 -*-
# @Time    : 17-11-14 下午10:01
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : first.py
# @Describe:
# @Software: PyCharm

import urllib2

request= urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
print response.read()


# urlopen(url, data, timeout)
