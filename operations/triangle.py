import numpy as np

class Triangle(object):
	"""docstring for Triangle"""
	
	def __init__(self, v1, v2, v3, norm="None"):
		super(Triangle, self).__init__()
		self.v1 = v1
		self.v2 = v2
		self.v3 = v3
		self.norm = norm