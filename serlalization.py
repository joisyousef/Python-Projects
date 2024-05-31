import pickle

hackers = {"neot":1,"geohot":100,"neo":1000}

for key, value in hackers.items():
	print(key, value)

serialised = pickle.dumps(hackers)
print(serialised)

deserialised_hackers = pickle.loads(serialised)
print(deserialised_hackers)

for key, value in deserialised_hackers.items():
	print(key, value)

#with open("hackers.pickle","wb") as handle:
#	pickle.dump(hackers, handle)

with open("hackers.pickle","rb") as handle:
	deserialised_hackers2 = pickle.load(handle)

print(deserialised_hackers2)