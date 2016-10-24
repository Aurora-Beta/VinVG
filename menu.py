# Menü

import pygame
import os
from pygame.locals import *

class menü(object):
	""" Das Menüobjekt. """
	def __init__(self, screen, renderer, bgcolor="0,0,0"):
		self.surface = screen
		self.r = renderer
		self.bgcolor = bgcolor
		self.Menühintergrund = self.r.get_image("Menu_Hintergrundbild",
												"Bilder/Menu/Hintergrund.png")
		self.Aktuelles_Menü = ""
		self.Aktuelle_Menükategorie = ""
		self.Menü_gezeichnet = False
		
		# Positionen der Menübuttons links
		self.Versatz_Y = self.surface.get_height() - self.r.get_size(self.Menühintergrund, "y")
		self.Versatz_X = 16
		self.Menü_Position_Knopf_1 = (self.Versatz_X, self.Versatz_Y + 16)
		self.Menü_Position_Knopf_2 = (self.Versatz_X + 40, self.Versatz_Y + 16)
		self.Menü_Position_Knopf_3 = (self.Versatz_X, self.Versatz_Y + 52)
		self.Menü_Position_Knopf_4 = (self.Versatz_X + 40, self.Versatz_Y + 52)
		self.Menü_Position_Knopf_5 = (self.Versatz_X, self.Versatz_Y + 88)
		
		# Buttons
		self.Menü_Buttons = []
		self.Button_Info = Button(			Name="Info", 
											Pfad="Bilder/Menu/Info.png",
											Position=self.Menü_Position_Knopf_1,
											Renderer=self.r,
											Funktion=self.Menü_Info)
									
		self.Button_Fahrzeuge = Button(		Name="Fahrzeuge",
											Pfad="Bilder/Menu/Fahrzeuge.png",
											Position=self.Menü_Position_Knopf_2,
											Renderer=self.r)
										
		self.Button_Linien = Button(		Name="Linien",
											Pfad="Bilder/Menu/Linien.png",
											Position=self.Menü_Position_Knopf_3,
											Renderer=self.r)
										
		self.Button_Haltestellen = Button(	Name="Haltestellen",
											Pfad="Bilder/Menu/Haltestelle.png",
											Position=self.Menü_Position_Knopf_4,
											Renderer=self.r)
		
		self.Button_Einstellungen = Button(	Name="Einstellungen",
											Pfad="Bilder/Menu/Einstellungen.png",
											Position=self.Menü_Position_Knopf_5,
											Renderer=self.r)
		
		
		self.add_Button(self.Button_Info,
						self.Button_Fahrzeuge,
						self.Button_Linien,
						self.Button_Einstellungen,
						self.Button_Haltestellen)

	def menü(self):
		self.surface.blit(self.Menühintergrund, (0, self.Versatz_Y))
		self.Buttons_Links_malen()
		self.Menü_Mitte_malen()
		self.Menü_Rechts_malen()
		
	def Buttons_Links_malen(self):
		if(self.Menü_Buttons != []):	# Wenn die Buttons NICHT leer sind ...
			for but in self.Menü_Buttons:
				self.surface.blit(but.get_image(), but.get_pos())

	def Menü_Mitte_malen(self):
		if(self.Aktuelles_Menü):
			if(self.Menü_gezeichnet == False):
				#if(self.Aktuelles_Menü == "Info"):
					#self.Info()
				print("Mitte")
				self.Menü_gezeichnet = True

	def Menü_Rechts_malen(self):
		None

	def set_Aktuelles_Menü(self, Wert):
		self.Aktuelles_Menü = Wert
		self.Menü_gezeichnet = False

	def Menü_Info(self):
		#self.Buttons_Links_malen()
		self.set_Aktuelles_Menü("Info")
		pass

	def get_Versatz_Y(self):
		return self.Versatz_Y

	def add_Button(self, *args):
		for but in args:
			self.Menü_Buttons.append(but)

	def rem_Button(self, *args):
		for but in args:
			self.Menü_Buttons.pop(but)

	def get_Buttons(self):
		return self.Menü_Buttons


class Button(object):
	""" Klasse für Buttons, mit der Möglichkeit bei Click eine Funktion auszuführen """
	def __init__(self, Position=[], Renderer=None,  Name="", Pfad="",  Funktion=None):
		self.r = Renderer
		self.pos = Position
		self.image = self.r.get_image(Pfad, Pfad)
		self.rect = Rect(Position, self.r.get_size(self.image))
		self.Name = Name
		self.Aktuelles_Menü = ""
		self.Funktion = Funktion

	def get_image(self):
		return self.image
	
	def get_rect(self):
		return self.rect
	
	def get_pos(self):
		return self.pos
	
	def get_name(self):
		return self.Name
	
	def collidepoint(self, pos):
		return self.rect.collidepoint(pos)
		
	def run(self):
		""" Die Funktion, die bei der Initialisierung übergeben wurde, wird nun ausgeführt,
		sofern überhaupt eine Funktion übergeben wurd. """
		if(self.Funktion):
			self.Funktion()
