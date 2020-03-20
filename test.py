import datetime
class Instrument:
	def sound(self):
		print("The instrument sounds")        
class Guitar(Instrument):
	i_range = 36
	polyphony = 6
	def sound(self):
		print("BRRRRRT")
class Drums(Instrument):
	i_range = -1
	polyphony = -1
	def sound(self):
		print("donk")        
class Piano(Instrument):
	i_range = 88
	polyphony = 88
	def sound(self):
		print("plin plin plon")
fender = Guitar();
schecter = Guitar();
schecter.polyphony = 7
schecter.i_range = 41
print(schecter.polyphony)
test1 = 55 / 4
print(test1)
test2 = int(test1)
print(datetime.datetime.now())
