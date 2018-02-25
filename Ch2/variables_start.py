# 
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

f=0
# print(f)

# f="abc"
# print(f)

# print ("test" + str(123))

def someFunction():
	global f
	f="def"
	print(f)

someFunction()
print(f)

del f
print(f)