import sqlite3


class datenbank(object):
	def __init__(self):
		self.connection = sqlite3.connect(":memory:")
		
	def get_con(self):
		return self.connection