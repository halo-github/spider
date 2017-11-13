#!/usr/bin/python

import Queue
import threading
import random

class myQueue:
	def __init__(self,queue,workers,method,proxies):
		self.queue = queue
		self.works = []
		self.target = method
		self.proxies = proxies
		for i in range(0,workers):
			self.works.append(threading.Thread(target = self.niceWork))
		##	print self.target,self.niceWork	


	def niceWork(self):
		while True :
			idx = random.randint(0,len(self.proxies)-1)
			proxy = self.proxies[idx]
			print proxy
			next = self.queue.get()
			self.target(next,proxy)
			self.queue.task_done()

	def startWork(self):
		for work in self.works:
			work.setDaemon(True)
			work.start()
		self.queue.join()
