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

imgPath = os.path.expanduser('~')+"/Pictures/"
	
		
		
def downImg(url):
        url = url.replace("\\","") 
	t = threading.current_thread()
	imgname = os.path.split(url)[1]
        try:
            	req = requests.get(url)
		headers = req.headers
		type = headers["Content-Type"]
		length = int(headers["Content-Length"])
		if str(type) == "image/jpeg" : 
	  		print t.getName()+" downloading "+url
        		with open(imgname,"wb") as pic:
                		pic.write(req.content)

        except Exception as e:
		print url
            	print e

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
	queue = Queue.Queue()
	spider = Spider(queue,keyWord,pages)
	spider.url_text()
	my_queue = myQueue(queue,int(threads),downImg)
	my_queue.startWork()
	et = time.time()
	print et - st
