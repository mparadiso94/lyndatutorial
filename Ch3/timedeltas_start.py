#
# Example file for working with timedelta objects
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print("today is:", now)
print("one year from now will be " + str( now + timedelta(days = 365)))
print("2 days and 3 weeks from now will be " + str( now + timedelta(days = 2, weeks = 3)))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("One week ago it was: %A %B %d, %Y")
print(s)

today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
	print("April fools day happened %d days ago" % ((today-afd).days))
	afd = afd.replace(year=today.year+1)

time_to_afd = afd - today
print("only", time_to_afd, "days until April Fools Day")