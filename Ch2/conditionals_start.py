#
# Example file for working with conditional statements
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
  x, y = 10, 100
  
  if(x < y):
  	st = "x is less than y"
  elif (x == y):
  	st = "x is equal to y"
  else:
  	st = "x is greater than y"

  print(st)

  st = "x is less than y" if (x<y) else "x is greater than or equal to y"
  print(st)

if __name__ == "__main__":
  main()
