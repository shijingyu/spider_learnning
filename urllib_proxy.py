# -*- coding: utf-8 -*-
# @Time    : 17-11-14 下午10:26
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : urllib_proxy.py
# @Describe:
# @Software: PyCharm
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8000'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

