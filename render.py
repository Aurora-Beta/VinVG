# render.py

import pygame
import os
from pygame.locals import *


class render(object):
	def __init__(self, karte, surface):
		self.versatz_x = 300
		self.versatz_y = 100
		self.image_cache = {}
		self.k = karte
		self.s = surface

	#
	# Scrollen
	#
	
	def scroll_up(self):
		self.versatz_y += 15

	def scroll_down(self):
		self.versatz_y -= 15

	def scroll_left(self):
		self.versatz_x += 15

	def scroll_right(self):
		self.versatz_x -= 15

	#
	# Cache-Funktionen
	#
	
	def add_to_cache(self, Bezeichnung, Inhalt):
		if not Bezeichnung in self.image_cache:
			self.image_cache[Bezeichnung] = Inhalt

	def del_from_cache(self, Bezeichnung):
		self.image_cache.delete(Bezeichnung)

	#
	# Bild-Funktionen
	#
	
	def get_image(self, Bezeichnung, Dateipfad):
		""" Bild aus dem Cache laden. """
		if not Bezeichnung in self.image_cache:
			self.add_to_cache(Bezeichnung, self.loadImage(Dateipfad))
			return self.image_cache[Bezeichnung]
		else:
			return self.image_cache[Bezeichnung]
	
	def loadImage(self, filepath, colorkey=None):
		""" Pygame das Bild laden lassen."""
		image = pygame.image.load(os.path.relpath(filepath, start=os.curdir))
		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
			if colorkey is not None:
				if colorkey is -1:
					colorkey = image.get_at((0,0))
				image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image


	def get_tile(self, Feld, tilekey, tilemap):
		""" Gibt Bild anhand des Symboles zurück und fügt es dem Cache zu,
		wenn es dort nicht bereits vorhanden ist. """
		dateiname = self.get_tile_bezeichnung(tilekey, Feld)
		if not dateiname in self.image_cache:
			if(dateiname == "Transparenz"):
				s = pygame.Surface((64,32), pygame.SRCALPHA)
				s.fill((255,255,255,0))
				self.add_to_cache(dateiname, s)
				return self.image_cache[dateiname]
			else:
				self.add_to_cache(dateiname, self.loadImage(self.get_tile_dateipfad(tilekey, Feld)))
				return self.image_cache[dateiname]
		else:
			return self.image_cache[dateiname]


	#
	#	Tile-Funktionen
	#
	
	def get_tile_bezeichnung(self, schlüssel, zeichen):
		""" Bezeichnung eines Symboles ermitteln. """
		for x in schlüssel:
			if x == zeichen:
				gleich = schlüssel[x]
				return gleich["bezeichnung"]

	def get_tile_dateipfad(self, schlüssel, zeichen):
		""" Dateipfad eines Symboles ermitteln. """
		for x in schlüssel:
			if x == zeichen:
				gleich = schlüssel[x]
				return gleich["pfad"]

	#
	#	Graphen / Ebenen
	#

	def hintergrund(self):
		"""" Rendert den Hintergrund. Wir generieren die Tile-Map und den Tile-Key,
		um die Hintergrundkarte zu rendern."""
		tilekey = self.k.get_tilekey(ebene="Hintergrund")
		tilemap = self.k.get_tilemap(ebene="Hintergrund")
				
		self.draw(self.s, tilekey, tilemap)

	def vordergrund(self):
		"""" Rendert den Vordergrund. Wir generieren die Tile-Map und den Tile-Key,
		um die Hintergrundkarte zu rendern. """
		tilekey = self.k.get_tilekey(ebene="Vordergrund")
		tilemap = self.k.get_tilemap(ebene="Vordergrund")
		
		self.draw(self.s, tilekey, tilemap)

	def get_size(self, tile, achse=""):
		if achse == "y":
			return((tile.get_rect().size)[1])
		elif achse == "x":
			return((tile.get_rect().size)[0])
		else:
			return(tile.get_rect().size)
		

	def draw(self, surface, tilekey, tilemap):
		""" Renderfunktion, die eine gegebene TileMap mit TileKey zeichnet """
		AktuelleZeile = 0
		AktuellesTile = 0

		for Zeile in tilemap:
			for Feld in Zeile:
				tile = self.get_tile(Feld, tilekey, tilemap)

				cartx = AktuellesTile * 64 / 2	# Index der X-Achse pro Tile
				carty = AktuelleZeile * 32  	# Index der Y-Achse pro Tile
				
				isox = self.versatz_x + ((cartx-carty))
				isoy = self.versatz_y + ((cartx+carty)/2) - self.get_size(tile, "y") 
				
				AktuellesTile += 1
				surface.blit(tile, (isox, isoy))	# Die Tile nun malen
			AktuellesTile = 0
			AktuelleZeile += 1

	def draw_Graph(self, Graph):
		""" Renderfunktion, die einen gegebenen Graph mit seinen Tiles zeichnet """
		AktuelleZeile = 0
		AktuellesTile = 0

		for Zeile in Graph.get_Knoten_as_Rows():
			for Knoten in Zeile:
				tile = Knoten.get_image()		# Darzustellendes Bild aus dem Knoten

				cartx = AktuellesTile * 64 / 2	# Index der X-Achse pro Tile
				carty = AktuelleZeile * 32  	# Index der Y-Achse pro Tile
				
				isox = self.versatz_x + ((cartx-carty))
				isoy = self.versatz_y + ((cartx+carty)/2) - self.get_size(tile, "y") 
				
				AktuellesTile += 1
				surface.blit(tile, (isox, isoy))	# Die Tile nun malen
			AktuellesTile = 0
			AktuelleZeile += 1

	def draw_Haltestelleninfos(self, Linien):
		for Haltestelle in Linien:
			print("TEST")

	def fahrzeuge(self):
		# Autos auslesen, berechnen und darstellen
		# Spielerfahrzeuge-Liste auslesen und jedes Fahrzeug durchgehen
		None
