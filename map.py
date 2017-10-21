# Kartenfunktionen

import configparser
import os
import graph

MAP_X = 12
MAP_Y = 12

class karte(object):
	def __init__(self, dateiname):
		self.tilemap_background = []
		self.tilemap_foreground = []
		self.tilemap_straßenbahn = []
		self.tilemap_sbahn = []
		self.tilemap_schwebebahn = []
		self.tilemap_magnetschwebebahn = []
		self.tilemap_fahrzeuge = []
		self.kartendatei = "missions/" + dateiname

		self.tilekey_background = {}
		self.tilekey_foreground = {}
		self.tilekey_fahrzeuge = {}
		self.MAP_X = 12
		self.MAP_Y = 12
		
		self.background = graph.Graph(self.MAP_X, self.MAP_X)
		self.foreground = graph.Graph(self.MAP_X, self.MAP_X)

	# Umrechnung von kartesischen Koordinaten in isometrische.
	def cart2iso(self, übergabe):
		cartX = übergabe[0]
		cartY = übergabe[1]
		isoX = 300 - (cartX)# - cartY)
		isoY = 100 - (cartX + cartY) / 2
		return isoX, isoY


	# Umrechnung von isometrischen Koordinaten in kartesische.
	def iso2cart(self, isoX, isoY): 
		cartX = (isoY + isoX) / 2;
		cartY = isoY - isoX;
		return cartX, cartY



	def load_tilemap(self, ebene=""):
		""" Tilemap wird aus Kartendatei geladen. """
		parser = configparser.ConfigParser()
		parser.read(os.path.relpath(self.kartendatei, start=os.curdir))
		if(ebene == "background"):
			rückgabe = parser.get("background", "background").split("\n")
		if(ebene == "foreground"):
			rückgabe = parser.get("foreground", "foreground").split("\n")
		return(rückgabe)


	# Hauptfunktion zum Generieren des Kartenobjektes
	def get_tilemap(self, ebene):
		"""Rückgabe eines iterierbaren Kartenobjektes.
		Dieses enthält in Zeilen die einzelnen Tile-Symbole.
		Zusammen mit dem Tile-Key kann man die Karte darstellen"""
		
		if(ebene == "background"):
			if(self.tilemap_background == []):		# Wenn die Karte leer ist, dann ...
				map = self.load_tilemap(ebene="background")
				self.tilemap_background = map
				return(self.tilemap_background)
			else:
				return(self.tilemap_background)
		
		if(ebene == "foreground"):
			if(self.tilemap_foreground == []):
				map = self.load_tilemap(ebene="foreground")
				self.tilemap_foreground = map
				return(self.tilemap_foreground)
			else:
				return(self.tilemap_foreground)
			

	def init_tilekey(self, parser, ebene=""):
		if(ebene != "background"):
			self.tilekey_foreground["."] = {
				"ebene": "foreground",
				"dateiname": "Transparenz",
				"bezeichnung": "Transparenz"}

		parser.read(os.path.relpath(self.kartendatei, start=os.curdir))
		for abschnitt in parser.sections():
			if len(abschnitt) == 1:
				desc = dict(parser.items(abschnitt))		# Alle Eigenschaften
				for schlüssel in desc:
					if(desc[schlüssel] == ebene):
						if(ebene == "foreground"):
							self.tilekey_foreground[abschnitt] = desc
						if(ebene == "background"):
							self.tilekey_background[abschnitt] = desc

	def get_tilekey(self, ebene=""):
		parser = configparser.ConfigParser()
		if(ebene == "foreground"):
			if(self.tilekey_foreground == {}):
				self.init_tilekey(parser, ebene="foreground")
				return(self.tilekey_foreground)
			else:
				return(self.tilekey_foreground)
		
		if(ebene == "background"):
			if(self.tilekey_background == {}):
				self.init_tilekey(parser, ebene="background")
				return(self.tilekey_background)
			else:
				return(self.tilekey_background)

class Tile(object):
	def __init__(self):
		self.image = None
		self.symbol = ""
	
	def get_image(self):
		return self.image
	
	def set_image(self, image):
		self.tile = image

# class Graph(object):
# 	def __init__(self):
# 		self.Knoten = []
# 		self.Verbindungen = {}
# 		self.Tiles = {}
# 		self.MAP_X = 12
# 		self.MAP_Y = 12
# 		
# 		for x in range(MAP_X):
# 			for y in range(MAP_Y):
# 				self.Knoten.append([x,y])
# 	
# 	def get_Knoten(self):
# 		return self.Knoten
# 
# 	def get_Knoten_as_Rows(self):
# 		sortiert = sorted(self.Knoten)
# 		temp = []
# 		zeile = []
# 		zähler = 0
# 		for element in sortiert:
# 			zeile.append(element)
# 			zähler += 1
# 			if(zähler % self.Zeilen == 0):
# 				temp.append(zeile)
# 				zeile = []
# 		return temp
# 
# 	def get_Verbindungen(self):
# 		return self.Verbindungen
# 	
# 	def set_Verbindung(self, Ausgangsknoten, Zielknoten):
# 		self.Verbindungen[str(Ausgangsknoten)] = Zielknoten
# 	
# 	def get_Verbindung2(self, Knoten):
# 		if(str(Knoten) in self.Verbindungen):			# Wenn es Verbindungen für den
# 			return self.Verbindungen[str(Knoten)]		# Knoten gibt, dann her damit!
# 	
# 	def get_Verbindung(self, Knoten):
# 		Richtungen = [[1,0], [0,1], [-1,0], [0,-1]]
# 		Ergebnis = []
# 		for Richtung in Richtungen:
# 			Nachbar = [Knoten[0] + Richtung[0], Knoten[1] + Richtung[1]]
# 			if(Nachbar in self.Knoten):
# 				Ergebnis.append(Nachbar)
# 		return Ergebnis
# 	
# 	def get_Tile(self, Knoten):
# 		return self.Tiles[str(Knoten)]
