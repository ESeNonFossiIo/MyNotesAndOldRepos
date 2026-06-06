###########
# Coloumn #
###########

class Column(object):
	"""Fill a coloumn."""
	def __init__(self, M, col):
		self.M = M
		self.numCol = col

	def check(self):
		"""This function check if it is possible to add a disk in the selected coloumn and returns the first free space if it is possible +1. (the +1 is to avoid return 0)"""
		column = self.M[self.numCol][:]
		for j in xrange(len(column)-1,-1,-1):
			if column[j] == 1:
				return j+1
		return False

	def add(self,val):
		self.M[self.numCol][self.check()-1]=val
