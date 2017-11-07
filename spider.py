#!/usr/bin/python
## -*- coding:utf-8 -*-ecoding : utf-8


import os
import re
import requests
from bs4 import BeautifulSoup
headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'Accept-Language':'zh-CN,zh;q=0.8',
		"referer":"https://image.baidu.com",
		'Accept':'text/plain, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Connection':'keep-alive',
		}

imgDir = "~/Picture/spiderPic"



kwd = raw_input("百度图片搜索关键字:")
pgs = raw_input("搜索页数：")
"""
"objURL":"http://c.hiphotos.baidu.com/image/pic/item/a50f4bfbfbedab643102c011fd36afc378311eea.jpg"
"""

url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord="+\
		str(kwd)\
		+"&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word="+\
		str(kwd)\
		+"&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl\
		&pn=450\
		&rn=60&gsm=96&1510035088334="
class Spider:
	def __init__(self):
		self.url = url + kwd
	
	def url_text(self):
		req = requests.get(url = self.url,headers = headers)
		list = re.findall(r'"ObjURL":"([^"]+)"',req.text)
		print list

class Downloader:
	def __init__(self):
		self.path =  imgDir + kwd



if __name__ == "__main__":
	spider = Spider()
	spider.url_text()
	downloader = Downloader()
	print spider.url
	print downloader.path
