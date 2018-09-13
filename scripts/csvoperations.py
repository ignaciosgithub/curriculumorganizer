import csv
import pandas
def write(row, filename, param1,param2,param3,param4,param5,param6):
 df = pandas.read_csv(filename)
 df.drop(df.index[row])
 append(filename,param1,param2,param3,param4,param5,param6)
def append(filename,param1,param2,param3,param4,param5,param6): 
 with open(filename, 'r+', newline='') as csvfile: 
  csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
  for rows in csvfile:

    csvwriter.writerow([param1,param2,param3,param4,param5,param6])
    break
 
def read(row, filename):
 allrows = []
 counter = 0
 if row == None:
  with open(filename, 'r+', newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   for rows in csvreader:
    allrows.append(rows)
   csvfile.close()
   return allrows

 












 else:

  with open(filename, 'r+', newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
   for rows in csvreader:
    counter = counter + 1
    if counter == row:
     return rows
    
   
   csvfile.close()
   
   return allrows
print(read(2,"tb.csv"))
write(2,"tb.csv","spaghetti","spaghetti","spaghetti","spaghetti","spaghetti","spaghetti")
print(read(None,"tb.csv"))









  




