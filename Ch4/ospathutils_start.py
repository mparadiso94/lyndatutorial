#
# Example file for working with os.path module
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
	# print(os.name)

	# print("item exists: " + str(path.exists("textfile.txt")))
	# print("item is a file: " + str(path.isfile("textfile.txt")))
	# print("item is a dir: " + str(path.isdir("textfile.txt")))

	# print("Item path: " + str(path.realpath("textfile.txt")))
	# print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

	# t = time.ctime(path.getmtime("textfile.txt"))
	# print(t)

	# print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
	td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
	print("it has been ", td, "since the file was modified")



if __name__ == "__main__":
	main()
