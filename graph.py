class Graph(object):
	def __init__(self, MAP_X, MAP_Y):
		self.Knoten = []
		self.Verbindungen = {}
		self.Tiles = {}
		self.Zeilen = MAP_X
		self.Spalten = MAP_Y
		self.clean()
	
	def clean(self):
	"""Alle Knoten werden gelöscht."""
		self.Knoten = []
		for x in range(self.Zeilen):
			for y in range(self.Spalten):
				self.Knoten.append([x,y])
	
	def get_Knoten(self):
	"""Gebe bestimmten Knoten zurück."""
		return self.Knoten

	def get_Knoten_Rows(self):
		sortiert = sorted(self.Knoten)
		temp = []
		zeile = []
		zähler = 0
		for element in sortiert:
			zeile.append(element)
			zähler += 1
			if(zähler % self.Zeilen == 0):
				temp.append(zeile)
				zeile = []
		return temp

	def get_Verbindungen(self):
		return self.Verbindungen
	
	def set_Verbindung(self, Ausgangsknoten, Zielknoten):
		self.Verbindungen[str(Ausgangsknoten)] = Zielknoten
	
	def get_Verbindung2(self, Knoten):
		if(str(Knoten) in self.Verbindungen):			# Wenn es Verbindungen für den
			return self.Verbindungen[str(Knoten)]		# Knoten gibt, dann her damit!
	
	def get_Verbindung(self, Knoten):
		Richtungen = [[1,0], [0,1], [-1,0], [0,-1]]
		Ergebnis = []
		for Richtung in Richtungen:
			Nachbar = [Knoten[0] + Richtung[0], Knoten[1] + Richtung[1]]
			if(Nachbar in self.Knoten):
				Ergebnis.append(Nachbar)
		return Ergebnis

class Tile(object):
	def __init__(self):
		self.image = None
		self.symbol = ""
	
	def get_image(self):
		return self.image
	
	def set_image(self, image):
		self.image = image
	
	def set_symbol(self, symbol):
		self.symbol = symbol
	
	def get_symbol(self):
		return self.symbol

