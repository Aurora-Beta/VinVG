

class Ampel(object):
	""" Ein Ampelobjekt, das die zwei Zustände "Fahrt" über True und "Stop" über False
	darstellt.
	"""
	def __init__(self):
		self.Fahrt = False
	
	def switch(self):
		if(self.Fahrt == False):
			self.Fahrt = True
		else:
			self.Fahrt = False
	
	def get_Status(self):
		return self.Fahrt