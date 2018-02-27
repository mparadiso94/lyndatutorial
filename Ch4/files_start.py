#
# Read and write files using the built-in Python file methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():  
	f = open("textfile.txt","r")
	# for i in range(10):
	# 	f.write("This is line " + str(i))

	# f.close()

	if f.mode == 'r':
		#contents = f.read()
		fl = f.readlines()
		for x in fl:
			print(x)
		# print(contents)


if __name__ == "__main__":
	main()
