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
	def __str__(self):
		return "My name is {} and I am {} years old.".format(self.name,self.age)
	def __add__(self,other):
		return self.age + other.age
	def __lt__(self,other):
		return self.age < other.age

bob = person("bob",30)
alice = person("alice",20)
print(bob)
print(bob+alice)
print(bob+bob)

print(bob<alice)
print(alice<bob)