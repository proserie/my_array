from statistics import median
from array import array

class Array:
	'''
	This is a single-dimensional numeric array for scientific computing.

	This array will compute lots of basic statics

	Parameters
	----------
	data: list
		List of numbers
	'''


	def __init__(self, data):
		self.data = array('d', data)

	def sum(self):
		'''
		Sums all the valuses in the array

		Returns
		-------
		int or float
		'''
		return sum(self.data)

	def min(self):
		'''
		Returns the smallest value in the array

		Returns
		-------
		int or float
		'''
		return min(self.data)

	def max(self):
		'''
		Returns the highest value in the array

		Returns
		-------
		int or float

		'''
		return max(self.data)

	def median(self):
		'''
		Returns the median value in the array

		Returns
		-------
		int or float
		'''
		return median(self.data)

	def mean(self):
		'''
		Returns the mean value in the array

		Returns
		-------
		int or float
		'''
		return self.sum() / len(self.data)
