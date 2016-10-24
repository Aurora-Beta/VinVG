# Linien


class Linien(object):
	""" Das Objekt zur Linienverwaltung. """

	def __init__(self):
		self.Linien = []
		self.Haltestellen = []
	
	def get_Linien(self, typ="alle"):
		None

	def get_Linie(self, Linien_ID):
		None

	def add_Linie(self, Transportmittel="", Pfad=[]):
		None

	def add_Haltestelle(self):
		None
		
	def get_Haltestellen_Schablone(self):
		temp = {}
		temp[Haltestellen_ID] = self.get_Haltestellen_ID()


class Linie(object):
	""" Linienobjekt """
	def __init__(self):
		self.Linien_ID = 0
		self.Transportmittel = ""
		self.Fahrzeuge = []