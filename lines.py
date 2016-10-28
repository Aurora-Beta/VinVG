# lines


class lines(object):
	""" Object which stores and manages all lines.  """

	def __init__(self):
		self.lines = []
		self.stops = []
	
	def get_all_lines(self):
		None

	def get_line(self, line_ID):
		None

	def add_line(self, transportation, path=[]):
		None

	def add_stop(self):
		None
		
	def get_stop_template(self):
		temp = {}
		temp[stop_ID] = self.get_gen_stop_ID()


class line(object):
	""" linenobject """
	def __init__(self):
		self.line_ID = 0
		self.transportation = ""
		self.vehicles = []
