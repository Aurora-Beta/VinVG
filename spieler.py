# Spieler.py



class spieler(object):
	def __init__(self):
		self.Kapital = 300000
		self.Name = "Spieler"
		self.Farbe = "Rot"

	def get_Kapital(self):
		return self.Kapital

	def get_Name(self):
		return self.Name

	def get_Farbe(self):
		return self.Farbe

	def add_Kapital(self, Geldbetrag):
		self.Kapital =+ Geldbetrag

	def sub_Kapital(self, Geldbetrag):
		self.Kapital =- Geldbetrag
