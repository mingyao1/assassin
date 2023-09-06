import csv
import random

filename = input("Please input the filepath for a CSV containing your target list> ")

if filename[0] == "'" and filename[-1] == "'":
  filename = filename[1:-1]

players = []

with open(filename, newline='') as f:
  file = csv.reader(f)
  #   for row in c:
  #   print(', '.join(row))
  #   players.append(row)
  for row in file:
        # Handle each row here
    cleaned_row = [field.strip() for field in row]  # Remove leading/trailing spaces
    
    if not cleaned_row:
        continue  # Skip empty lines
    print(', '.join(row))
    players.append(row)

random.shuffle(players)
start = players[0]

with open("outfile.csv", 'w') as o:
  output = csv.writer(o)
  for i in range(0, len(players)-1):
    output.writerow((players[i], players[i+1]))
  output.writerow((players[-1], players[0]))
