#
# Example file for working with Calendars
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


import calendar

c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2018, 1, 0, 0)
print(st)


