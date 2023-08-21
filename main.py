import csv

filename = input("Please input the filepath for a CSV containing your target list> ")

with open(filename, 'r') as f:
  csv = csv.reader(f)
  for row in csv:
    print(', '.join(row))

#insert remaining code here
