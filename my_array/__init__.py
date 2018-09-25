from statistics import median


class Array:


	def __init__(self, data):
		self.data = data

	def sum(self):
		return sum(self.data)

	def min(self):
		return min(self.data)

	def max(self):
		return max(self.data)

	def median(self):
		return median(self.data)

	def mean(self):
		return self.sum() / len(self.data)
