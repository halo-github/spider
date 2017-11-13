#!/usr/bin/python
#**coding:utf-8


import re
import requests as req
import random


def proxy_list():
	ranPage = random.randint(0,10)
	url = "http://www.kuaidaili.com/ops/proxylist/"+str(ranPage)+"/"
	headers = {
			'accept-encoding' : 'gzip,deflate',
			'accept-language' : 'zh-cn,zh;q=0.8',
			'host':'www.kuaidaili.com',
			'referer' : 'http://www.kuaidaili.com/ops/proxylist/1/',
			'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
			}
	text = req.get(url = url,headers = headers).text
#	print text
	reg = r'"IP">([0-9]{2,3}.[0-9]{2,3}.[0-9]{2,3}.[0-9]{2,3}).*\n.*"PORT">([0-9]{,4}).*\n.*\n.*>(HTT.*)<.*\n'
	list = re.findall(reg,text)
#	print lit
	proxies = []
	for i in list:
		dic = {}
		keys = str(i[2]).split(", ")
		for key in keys:
			dic[key] = str(i[0])+":"+str(i[1])
		proxies.append(dic)
#	print proxies
	return proxies	
		
if __name__ == '__main__':
	proxy_list()

