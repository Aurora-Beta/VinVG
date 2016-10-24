# Fahrzeuge

class Fahrzeuge(object):
	""" Die Klasse für die Fahrzeuge. """
	def __init__(self):
		self.Liste_Fahrzeuge_im_Spiel = {}
		self.Liste_Autos = {}
		self.Liste_Verfügbare_Fahrzeuge = {}
		self.Liste_Fahrzeuge_im_Depot = {}

	def Fahrzeug_ID_generieren(self):
		t = Self.Liste_Autos + Self.Liste_Fahrzeuge_im_Depot + Self.Liste_Fahrzeuge_im_Spiel
		if(t):
			zähler = 1
			for Fahrzeuge in t:
				id = Fahrzeuge["Fahrzeug_ID"]
				if(id >= zähler):
					zähler = id
			return(zähler + 1)
		else:
			return 1


	def Fahrzeug_Kaufen(self, Fahrzeugmodell_ID):
		self.Add_Fahrzeug(Fahrzeug)
		None

	def Add_Fahrzeug(self, Fahrzeug):
		None
	
	def Del_Fahrzeug(self, Fahrzeug_ID):
		None
	
	def Verkaufe_Fahrzeug(self, Fahrzeug_ID):
		None
	
	def get_Fahrzeug(self, Fahrzeug_ID):
		temp = self.Liste_Fahrzeuge_im_Depot + self.Liste_Fahrzeuge_im_Spiel
		return temp[Fahrzeug_ID]
	


class Fahrzeug(object):
	def __init__(self, Linie=None, Fahrzeug_Art_ID=0, Route=[]):
		# Übergebene Parameter
		self.Fahrzeug_Art_ID = Fahrzeug_Art_ID
		self.Linie = Linie
		self.Route = Route
		
		# Implizite Parameter
		self.Fahrzeug_ID = 0
		self.Zustand = 100
		self.Geschwindigkeit = 0
		self.Sitzplätze = 0
		self.Fahrgäste = {}
		self.Datum_Gekauft = (0,0)
		self.Voll = False
	
	def Einsteigen(self, Personen):
		for Fahrgast in Personen:
			self.Fahrgäste.append(Fahrgast)