class Deque:

	def __init__(self):
		self.deque = []
		self.len = 0

	def empty(self):
		if self.len == 0:
			return True
		return False

	def push_front(self, n):
		self.deque.insert(0, n)
		self.len += 1

	def push_back(self, n):
		self.deque.insert(self.len, n)
		self.len += 1

	def pop_front(self):
		if self.len > 0:
			self.deque.pop(0)
			self.len -= 1

	def pop_back(self):
		if self.len > 0:
			self.deque.pop(self.len -1)
			self.len -= 1

	def front(self):
		if self.len > 0:
			return self.deque[0]
		return None	

	def back(self):
		if self.len > 0:
			return self.deque[self.len - 1]
		return None

	def show(self):
		for i in self.deque:
			print(i)