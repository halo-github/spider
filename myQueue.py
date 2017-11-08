#!/usr/bin/python

import Queue
import threading

class myQueue:
	def __init__(self,list,workers,target):
		self.queue = Queue.Queue()
		for i in list:
			self.queue.put(i)
		self.works = []
		self.target = target
		for i in range(0,workers):
			self.works.append(threading.Thread(target = self.niceWork))
		##	print self.target,self.niceWork	


	def niceWork(self):
		while True :
			next = self.queue.get()
			self.target(next)
			self.queue.task_done()

	def startWork(self):
		for work in self.works:
			work.setDaemon(True)
			work.start()
		self.queue.join()
