# Menschen.py

class Mensch_Objekt(object):
	def __init__(self, Typ, Wohnung, Ziel):
		self.ID = 1
		self.Typ = Typ
		self.Wohnung = Wohnung
		self.Ziel = Ziel
		None

class Menschen(object):
	def __init__(self):
		self.Anzahl_Schüler = 0
		self.Anzahl_Berufstätiger = 0
		self.Anzahl_Freizeit = 0
		self.Anzahl_Einkauf = 0

		self.Schüler = {}
		self.Berufstätiger = {}
		self.Freizeit = {}
		self.Einkauf = {} 
		