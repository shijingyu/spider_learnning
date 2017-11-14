# -*- coding: utf-8 -*-
# @Time    : 17-11-14 下午10:07
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : second.py
# @Describe:
# @Software: PyCharm
import urllib,urllib2

values = {"username":"1234567@qq.com","password":"XXXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

