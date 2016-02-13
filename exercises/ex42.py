# Exercise 42: Is-A, Has-A, Objects, and Classes

## Ideally, you should define your classes in separate file, then you should
## import them in your main program file using import statement.


## Animal is-an object (yes, sort of confusing) look at the extra credit
class Animal(object):
	# The pass statement is a null operation used when a statement is required
	# syntactically but you do not want any command or code to execute in
	# places where your code will eventually go, but has not been written yet
	pass
	
		
## class Dog is-an Animal
## class Dog has-an __init__ (constructor method) that take self and name as 
## parameters
class Dog(Animal):

	def __init__(self, name):
		## Dog has-an attribute name set to name
		self.name = name


## class Cat is-an Animal
## class Cat has-an __init__ (constructor method) that takes self and name 
## parameters
class Cat(Animal):

	def __init__(self, name):
		## Cat has-an attribute name set to name
		self.name = name


## class Person is-a class
## class Person has-an __init__ (constructor method) that takes self, name,
## salary parameters
class Person(object):
	
	def __init__(self, name):
		## Person has-an attribute name set to name
		self.name = name
		
		## Person has-an attribute pet set to None
		## None is a built-in constant frequently used to represent the absence
		## of a value, as when default arguments are not passed to a function
		self.pet = None
		
## class Employee is-a Person
## class Employee has-an __init__ (constructor method) that takes self, name, 
## salary as parameters
class Employee(Person):

	def __init__(self, name, salary):
		## runs the __init__ method of a parent class reliably
		super(Employee, self).__init__(name)
		## class Employee has-an attribute salary set to salary
		self.salary = salary


## Fish is-a class
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("Rover")
## satan is-an instance of Cat
satan = Cat("Satan")
## mary is-an instance of Person
mary = Person("Mary")
## mary has-an attribute pet set to 'satan'
mary.pet = satan
## frank is-an instance of Employee with the parameters of name and salary set to
## "Frank" and 120000 (respectively)
frank = Employee("Frank", 120000)
## the instance frank has-a attribute pet set to rover
frank.pet = rover
## flipper is-an instance of Fish()
flipper = Fish()
## crouse is-a Salmon()
crouse = Salmon()
## harry is-a Halibut()
harry = Halibut()
