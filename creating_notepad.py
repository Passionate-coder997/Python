from pathlib import Path
path=Path()
print('''path.glob("*")''')#this will create generator object for which we can iterate through it.
for file in path.glob("*"):
	print(file)
#print(path.mkdir())
#print(path.rmdir())