class Queue:

	def __init__(self):
		self.queue = []
		self.len_queue = 0

	def push(self, n):
		self.queue.append(n)
		self.len_queue += 1

	def pop(self):
		if self.len_queue > 0:
			self.queue.pop(0)
			self.len_queue -= 1

	def empty(self):
	    if self.len_queue == 0:
	        return True
	    return False

	def length(self):
		return self.len_queue

	def front(self):
		if self.len_queue > 0:
			return self.queue[0]
		return None