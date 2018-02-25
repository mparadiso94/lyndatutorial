#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


from datetime import date
from datetime import time
from datetime import datetime

def main():
	# today = date.today()
	# print("The date today is ", today)

	# print("componenets: ", today.day, today.month, today.year)
	
	# print("Today's week day number is : ", today.weekday())

	# days = ["mon","tue","wed","thu","fri","sat","sun"]

	# print("which is a:", days[today.weekday()])

	today = datetime.now()
	print("time and date", today)

	t = datetime.time(datetime.now())
	print(t)

if __name__ == "__main__":
	main();