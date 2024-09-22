def print_out(a):
	print("outer {}".format(a))

	def print_in():
		print("\tinner {}".format(a))

	return print_in

test = print_out("test")
del print_out
test()
