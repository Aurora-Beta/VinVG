class ID(object):
	def __init__(self):
		self.ID = 0
		
	def get_ID(self):
		self.ID += 1
		return self.ID
	
	
class Einwohner(object):
	def __init__(self, Funktion=None, Ziel=None):
		self.ID = Funktion()
		self.Name = "Testeinwohner"
		self.Ziel = Ziel
	
	def get_ID(self):
		return self.ID

	def get_Name(self):
		return self.Name
	
	def set_Ziel(self, Ziel):
		self.Ziel = Ziel


class Bus(object):
	def __init__(self):
		self.Kapazität = 30
		self.Passagiere = []
		self.Voll = False
		self.Route = []
	
	def Einsteigen(self, Passagier):
		self.Passagiere.append(Passagier)
		
	def Aussteigen(self, Passagier):
		return self.Passagiere(Passagier)
	
	def get_Passagiere(self):
		return self.Passagiere

	def set_Route(self, Route):
		self.Route = Route

class Haltestelle(object):
	def __init__(self):
		self.Leute = []
		self.Einzugsbereich = ["Schule"]
	
	def add_Leute(self, Leute):
		self.Leute.append(Leute)

	def rem_Leute(self, Leute):
		self.Leute.remove(Leute)


class Linie(object):
	def __init__(self):
		self.Haltestellen = []
		self.Fahrzeuge = []
		self.Route = []
	
	def add_Fahrzeug(self, Fahrzeug):
		self.Fahrzeuge.append(Fahrzeug)
	
	def del_Fahrzeug(self, Fahrzeug):
		self.Fahrzeuge.remove(Fahrzeug)
	
	def add_Haltestelle(self, Haltestelle):
		self.Haltestellen.append(Haltestelle)
	
	def get_Fahrzeuge(self):
		return self.Fahrzeuge
	
	def get_Haltestellen(self):
		return self.Haltestelle
	
	def set_Route(self, Route):
		self.Route = Route
		for Fahrzeug in self.Fahrzeuge:
			Fahrzeug.set_Route(self.Route)


def gen_Einwohner(Anzahl, Funktion=None, Ziel=None):
	temp = []
	for x in range(0, Anzahl):
		a = Einwohner(Funktion, Ziel)
		temp.append(a)
	return temp

id = ID()

Haltestelle1 = Haltestelle()
Haltestelle1.add_Leute(gen_Einwohner(500, Funktion=id.get_ID, Ziel="Haltestelle2"))
Haltestelle2 = Haltestelle()

Linie1 = Linie()
Linie1.add_Haltestelle(Haltestelle1)
Linie1.add_Haltestelle(Haltestelle2)

MAP_X = 4
MAP_Y = 4

import graph

Straße = graph.Graph(MAP_X, MAP_Y)
Straße.set_Verbindung([2,2], [[2,3], [2,1]])
#print(Straße.get_Knoten())
#print(Straße.get_Verbindung([0,0]))

print(Straße.get_Verbindung2([2,2]))
t = Straße.get_Knoten_Rows()
for row in t:
	print(row)
