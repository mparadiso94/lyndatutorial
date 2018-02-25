#
# Example file for working with classes
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
class myClass():
	def method1(self):
		print("my class method 1")

	def method2(self, someString):
		print("method 2: " + someString)

class anotherClass(myClass):
	def method1(self):
		myClass.method1(self)
		print("another class method 1")

	def method2(self, someString):
		print("another class method 2: ")
      
def main():
	c = myClass()
	c.method1()
	c.method2("string to print!")

	c2 = anotherClass()
	c2.method1()
	c2.method2("another string to print :)")

if __name__ == "__main__":
	main()
