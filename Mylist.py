class MyList(list):
	def remove_min(self):
		self.remove(min(self))
	def remove_max(self):
		self.remove(max(self))

x = [1,2,3,4,5,6,7,8,9,10]
y = MyList(x)