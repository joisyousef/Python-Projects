class person:
	'person base class'
	wants_to_hack = True

	def __init__(self, name, age):
		self.name = name
		self.age = age
	def print_name(self):
		print("My name is {}".format(self.name))

	def print_age(self):
		print("My age is {}".format(self.age))

	def birthday(self):
		self.age += 1

bob = person("bob",30)
alice = person("alice",20)
mallory = person("mallory",50)

print(bob)
print(alice)
print(mallory)

bob.print_name()
alice.print_name()
mallory.print_name()

bob.print_age()
alice.print_age()
mallory.print_age()
 
bob.age = 31
bob.print_age()

bob.birthday()
bob.print_age()
print(bob.name)
print(bob.age)

print(hasattr(bob,"age"))
print(hasattr(bob,"asd"))

print(getattr(bob,"age"))

setattr(bob,"asd",100)
print(getattr(bob,"asd"))

delattr(bob,"asd")

#print(getattr(bob,"asd"))

print(person.wants_to_hack)

person.wants_to_hack = "No way!"

print(person.wants_to_hack)

bob.print_name()
del bob.name
#bob.print_name()

#del person
#print(alice.name)
#print(alice.print_name())

bob2 = person("bob2",35)
 
print(person.__dict__)
print(person.__doc__)
print(person.__name__)
print(person.__module__)