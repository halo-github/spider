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

imgPath = os.path.expanduser('~')+"/Pictures/"
	
		
		
def downImg(url):
	url = url.replace("\\","")
##	print ss
##        ll = url.split("\\")
##        url =  "".join(ll)
	t = threading.current_thread()
	imgname = os.path.split(url)[1]
        try:
            data = requests.get(url).content
        except:
            print "exception"
        else:    
	    print t.getName()+" downloading "+url
            with open(imgname,"wb") as pic:
                pic.write(data)
            		

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
	spider = Spider(keyWord,pages)
	print spider.url
	imgList = spider.url_text()
	my_queue = myQueue(imgList,int(threads),downImg)
	my_queue.startWork()
	et = time.time()
	print et - st
