#!/usr/bin/python
#*-*coding:utf-8
#encoding:utf-8


import os
from spider import Spider
import Queue
import threading
from myQueue import myQueue
import time
import requests
import sys
from proxy import proxy_list



imgPath = os.path.expanduser('~')+"/Pictures/"

time_out = 3     ##下载tiemout 
	
		
		
def downImg(url,proxy):
	headers = {
                                 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome    /61.0.3163.100 Safari/537.36', 'Accept-Language':'zh-CN,zh;q=0.8',
	          		 "referer":"https://image.baidu.com",
 	                         'Accept':'text/plain, */*; q=0.01',
				 'Accept-Encoding':'gzip, deflate, br',
				 'Connection':'close',
			                                       }
       
	
	url = url.replace("\\","") 
	t = threading.current_thread()
	imgname = os.path.split(url)[1]
        try:
            	req = requests.get(url = url, headers = headers,proxies = proxy,timeout = time_out)
		headers = req.headers
		type = headers["Content-Type"]
		if str(type) == "image/jpeg" : 
			length = int(headers["Content-Length"])
			if length and length > 20000:
        			with open(imgname,"wb") as pic:
                			pic.write(req.content)
	  			print t.getName()+" --- "+url
        except Exception as e:
            	print "***" 
		print e
		print url
		print "-------------------"

if __name__ == "__main__":
	keyWord = raw_input("请输入百度图片搜索关键字：")
	pages = raw_input("请输入搜索页数：")
	threads = raw_input("请输入下载线程数量：")
	
	cwd = os.getcwd()
	imgDir = imgPath+keyWord
	if not os.path.exists(imgDir):
		os.mkdir(imgDir)
	os.chdir(imgDir)
	st = time.time()
	proxies = proxy_list()

	queue = Queue.Queue()
	spider = Spider(queue,keyWord,pages)
	spider.url_text()
	my_queue = myQueue(queue,int(threads),downImg,proxies)
	my_queue.startWork()
	et = time.time()
	print "用时：" + str(et - st)
