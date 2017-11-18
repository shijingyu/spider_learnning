# -*- coding: utf-8 -*-
# @Time    : 17-11-18 下午9:00
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : QSBK.py
# @Describe:
# @Software: PyCharm
import re
import urllib2


class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
        self.headers = {'User-Agent': self.user_agent}
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
    #传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            url ='http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的ｒｅｑｕｅｓｔ
            request = urllib2.Request(url, headers = self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"链接糗事百科失败，错误原因", e.reason
                return None

    #传入某一页代码，返回本页段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败..."
            return None
        pattern = re.compile('<h2>(.*?)</h2>.*?content">.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>',re.S)
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            #创建匹配实例
            replaceBR = re.compile('</br>')
            #把</br>替换成\n
            text = re.sub(replaceBR,"\n",item[1])
            pageStories.append([item[0].strip(),text.strip(),item[2].strip()])
        return pageStories

    #加载并提取页面的内容，加入到列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    #获取完之后页码索引加１，表示下次读取下一页
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        for story in pageStories:
            #等待用户输入
            input = raw_input()
            if input !="Q":
                self.loadPage()
            if input == "Q":
                self.enable = False
                return
                print u"第%d页\t发布人:%s\t赞:％s\n%s" %(page,story[0],story[2],story[1])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        if len(self.stories)>0:
            #从全局list中获取一页的段子
            pageStories = self.stories[0]
            #当前读到的页数加一
            nowPage += 1
            #将全局list中第一个元素删除，因为已经取出
            del self.stories[0]
            #输出该页的段子
            self.getOneStory(pageStories,nowPage)

if __name__ == '__main__':
    spider = QSBK()
    spider.start()
