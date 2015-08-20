

import numpy as np

v = np.array([1,2,3])

class boom:

	def __init__(self,data):
		self.data=data
	def modi(self,vector):
		vector[0]=100
		return vector

boomer = boom("ihateyou")

modifiedv = boomer.modi(v)

print(modifiedv)