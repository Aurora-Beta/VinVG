#
# Class for buildings containing people
#



class all_buildings(object):
	def __init__(self, database):
		self.livinghouse = {}
		self.schools = {}
		self.workplaces = {}


class building(object):
	def __init__(self, type=""):
		self.id = None
