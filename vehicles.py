# Fahrzeuge

class all_vehicles(object):
	""" This class inherits all vehicles. """
	def __init__(self):
		self.all_npc_vehicles = {}	# Cars of inhabitants
		self.vehicles_ingame = {}	# Vehicles in game
		self.vehicles_standby = {}	# Vehicles in depot

	def gen_vehicle_id(self):
		""" Generates an unique ID for vehicles. """
		t = Self.all_npc_vehicles + Self.vehicles_ingame + Self.vehicles_standby
		if(t):
			counter = 1
			for vehicles in t:
				id = Vehicle["vehicle_id"]
				if(id >= counter):
					counter = id
			return(counter + 1)
		else:
			return 1



class Vehicle(object):
	""" Object-class for every vehicle. """
	def __init__(self, Line=None, Vehicle_class_ID=0):
		# Parameters given
		self.Vehicle_class_ID = Vehicle_class_ID
		self.Line = Line
		
		# Implicit or generated parameters
		self.Vehicle_ID = 0
		self.Condition = 100
		self.Velocity = 0
		self.Seats = 0
		self.Passengers = {}
		self.Date_buy = (0,0)
		self.is_full = False
	
