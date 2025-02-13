import sys 

class Queue:
	def __init__(self):
		self.queue = []
		self.maxlen = sys.maxsize
	
	def enqueue(self, val):
		if self.full():
			raise Exception
		self.queue = self.queue + [val]	
	
	def dequeue(self):
		if self.empty():
			raise Exception
		val = self.queue[-1]
		del self.queue[-1]
		return val
	
	def head(self):
		if self.empty():
			raise Exception
		return self.queue[-1]

	def tail(self):
		if self.empty():
			raise Exception
		return self.queue[0]

	def full(self):
		if len(self.queue) == self.maxlen:
			return True
		return False

	def empty(self):
		if len(self.queue) == 0:
			return True
		return False

	def length(self):
		return len(self.queue)

	def __str__(self):
		return str(self.length()) + ', ' + str(self.queue)
