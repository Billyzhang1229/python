class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descripitive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can not roll back an odometer.")

	def incrment_odometer(self, miles):
		self.odometer_reading += miles

my_used_car = Car('subaru', 'outbreak', 2013)
print(my_used_car.get_descripitive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.incrment_odometer(100)
my_used_car.read_odometer()