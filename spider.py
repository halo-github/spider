#!/usr/bin/python
## -*- coding:utf-8 -*-ecoding : utf-8


import re
import requests
class Spider:
	def __init__(self,keyword,pages):
	
		self.headers = {
				'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36', 'Accept-Language':'zh-CN,zh;q=0.8',
				"referer":"https://image.baidu.com",
				'Accept':'text/plain, */*; q=0.01',
				'Accept-Encoding':'gzip, deflate, br',
				'Connection':'keep-alive',
				}

		imgDir = "~/Picture/spiderPic"



		"""
		"objURL":"http://c.hiphotos.baidu.com/image/pic/item/a50f4bfbfbedab643102c011fd36afc378311eea.jpg"
		"""

		url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord="+\
				str(keyword)\
				+"&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word="+\
				str(keyword)\
				+"&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=girl&pn="+\
				str(int(pages)*30)\
				+"&rn=60&gsm=96&1510035088334="
		self.url = url 
	def url_text(self):
		req = requests.get(url = self.url,headers = self.headers)
		list = re.findall(r'"ObjURL":"([^"]+)"',req.text)
##		for i  in list:
##			print i
		return list



