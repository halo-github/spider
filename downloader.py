#!/usr/bin/python
#*-*coding:utf-8
#encoding:utf-8

imgPath = "~/Pictures/"


import os
from spider import Spider
import Queue
import threading
from myQueue import myQueue
import time

##class Downloader:
##	def __init__(self,list,workers):
##		self.queue = myQueue(list,workers,downImg) 
	
		
		
def downImg(url):
	t = threading.current_thread()
	print t.getName()+" downloading "+url
	imgname = os.path.split(url)(1)
	print imgname
		

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
