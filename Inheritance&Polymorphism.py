class Dog:
	def breed(self,val):
		self.val=val
		print(self.val)
	def bark(self):
		print('Whoow')

class Pet(Dog):#pet class inherits Dog() class
	def name(self):
		print("Dog's Name: Moti")
	

person=Pet()
tommy=Dog()

person.name()
person.bark()
person.breed('German Sheperd\n\n')
tommy.breed('pomerian')
tommy.bark()


#polymorphism
class Mobile:
	def type():
		print('An electronic device')


	def color():
		print('Black color')

class Laptop(Mobile):
	def color():
		print("White color")


def color(poly):
	poly.type()
	poly.color()


sm=Mobile()
lm=Laptop()

color(Mobile)
color(Laptop)