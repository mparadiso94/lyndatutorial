# 
# Example file for parsing and processing JSON
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
import urllib.request
import json


def printResults(data):
		theJson = json.loads(data)

		# if "title" in theJson["metadata"]:
		# 	print(theJson["metadata"]["title"])

		# count = theJson["metadata"]["count"]
		# print(str(count), "events recorded")

		# for i in theJson["features"]:
		# 	print(i["properties"]["place"])  

		# print("------------------------")  

		# for i in theJson["features"]:
		# 	if i["properties"]["mag"] >= 4.0:
		# 		print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
		# print("------------------------")  

		for i in theJson["features"]:
			feltreports = i["properties"]["felt"]
			if feltreports != None and feltreports > 0:
				print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], "reported ", str(feltreports), "times")

def main():
	# define a variable to hold the source URL
	# In this case we'll use the free data feed from the USGS
	# This feed lists all earthquakes for the last day larger than Mag 2.5
	urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

	webUrl = urllib.request.urlopen(urlData)
	print ("result code: " + str(webUrl.getcode()))
	if(webUrl.getcode() == 200):
		data = webUrl.read()
		printResults(data)
	else:
		print("Recieved an error getting the url")
  

if __name__ == "__main__":
	main()
