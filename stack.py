class Stack:
	def __init__(self):
		self.stack = []
		self.len_stack = 0

	def push(self, n):
		self.stack.append(n)
		self.len_stack += 1

	def pop(self):
		if self.len_stack > 0:
		    self.stack.pop(self.len_stack -1)
		    self.len_stack -= 1

	def top(self):
		if self.len_stack > 0:
		    return self.stack[-1]
		return None

	def empty(self):
		if(self.len_stack == 0):
			return True
		return False

	def length(self):
		return self.len_stack

if __name__ == "__main__":
	s = Stack()

	print(s.length())
	print(s.top())
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	print(s.top())
	print(s.empty())
	s.pop()
	print(s.top())
	print(s.length())
