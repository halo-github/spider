#!/usr/bin/python
## -*- coding:utf-8 -*-ecoding : utf-8


import re
import requests
class Spider:
	def __init__(self,queue,keyword,pages):
		self.queue = queue
		self.keyword = keyword
		self.pages = int(pages)
		self.headers = {
				'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'Accept-Language':'zh-CN,zh;q=0.8',
				"referer":"https://image.baidu.com",
				'Accept':'text/plain, */*; q=0.01',
				'Accept-Encoding':'gzip, deflate, br',
				'Connection':'keep-alive',
				}




		"""
		"objURL":"http://c.hiphotos.baidu.com/image/pic/item/a50f4bfbfbedab643102c011fd36afc378311eea.jpg"
		"""

	def url_text(self):
		i = int(0)
		while  i < self.pages:
			url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord="+\
					str(self.keyword)\
					+"&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word="+\
					str(self.keyword)\
					+"&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn="+\
					str(i*30)\
					+"&rn=30&gsm=96&1510035088334="
			self.url = url 
			req = requests.get(url = self.url,headers = self.headers)
			list = re.findall(r'"ObjURL":"([^"]+)"',req.text)
			for url in list:
				self.queue.put(url)
			i = i + 1



