import os
b = ""
for a in os.listdir("Funkodb"):
 f = open("Funkodb/"+a,"r")
 if(len(f.read().split()) == 1):
  f.seek(0)
  b = f.read()
  f.close()
  f = open("Funkodb/"+a,"w")
  b = b.replace("price"," price ").replace("Price"," Price ").replace("stockstate="," stockstate= ")
  f.write(b)
  print(a)
  f.close()
