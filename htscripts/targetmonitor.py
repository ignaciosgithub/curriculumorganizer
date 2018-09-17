from urllib.request import urlopen as uReq
import requests
import os
import bs4
from bs4 import BeautifulSoup as soup
import csv
import dryscrape
import re
import discordmsg
discordmsg.send("target monitor started")
nineteen = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
discordinfo = ""
discordinfo2 =""
databasename = "targetdatabase3.csv"
databasetextname = "tDatabase"
print(os.listdir("tDatabase"))
class Product:
 stockqty = ""
 pid = ""
 name = ""
 price = ""
 url = ""
 inStock = False
 imgurl = ""
 f = ""
 def get_price(self):
  if("https" not in self.url):
   return "invalid"
  print(self.url)
  uClient = requests.get(self.url)
  page_html = uClient.text
  uClient.close()
  newlist = []
  for a in page_html.split():
   if '"price":' in a:
    newlist.append(a)
    break
  for b in newlist:
   for c in b.split(":"):
  
    try:
     if '"priceCurrency"' in c:
      c=c.replace('"','')
      c = c.replace("priceCurrency","")
      c = c.replace(",","")
      self.price = c
      return c
    except:
     print(" ")  
  

  pass
 def get_stock(self):
  uClient = requests.get(self.url)
  page_html = uClient.text
  uClient.close()
  newlist = []
  for a in page_html.split():
   if('"isinStock":true' in a or '"isinStock":True' in a):
    print("in stock")
    
    self.inStock = True
    return True
  self.inStock = False
  return False 
 def get_imgurl(self):
  uClient = requests.get(self.url)
  page_html = uClient.text
  uClient.close()  
  for a in page_html.split(','):
   if('"imageUrl":' in a):
    imgurl = a.replace(",","").replace("imageUrl","").replace('"','').replace(":","")
    imgurl = "https://target.scene7.com/is/image/Target/"+self.pid
    return imgurl
    










def compareindatabase(examineurllist):
 previousstateofproduct = Product()
 keywords = []
 numofkeysfound = 0
 kf = open("keywords.txt","r")
 kftext = kf.read()
 keywords = kftext.split(",")
 usekeywords = False
 if(len(keywords) > 0):
  usekeywords = True
 htmlarray = []
 possibleproducturls = []
 searchurl = "https://www.target.com/p/sitemap_001.xml.gz"
 currproduct = Product()
 indatabase = False
 for counter in nineteen:
  if(counter <9):
   searchurl = "https://www.target.com/p/sitemap_00"+str(counter+1)+".xml.gz"
  else:
   searchurl = "https://www.target.com/p/sitemap_0"+str(counter+1)+".xml.gz" 
  uClient = requests.get(searchurl)
  page_html = uClient.text
  uClient.close()
  dirtyurls = []
  
  for c in page_html.split('\n'):
   if("<loc>" in c and "</loc>"):
    dirtyurls.append(c)
    
  for a in dirtyurls:
   numofkeysfound = 0
   a= a.replace('<loc>','').replace('</loc>','')
   if(usekeywords == True):
    for key in keywords:
     print(key)
     if(key in a and len(key) > 0):
      numofkeysfound = numofkeysfound+1
      break
    if(numofkeysfound == 0):
     print("here is continue")
     continue
   if(numofkeysfound != 0): 
    currproduct.url = a
    print(a + '[separator]')
    if("" == currproduct.url or '?xml version="1.0" encoding="UTF-8"?>' == currproduct.url or None == currproduct.url):
     continue
  
    for b in a.split("/"):
     if("www.target.com" or "https:" in b):

      continue
     else:
      if(len(b) > 1):
       if("A-" in b):
        currproduct.pid = b.replace("A-","")
       else:
        currproduct.name = b
      currproduct.get_price()
      currproduct.get_stock()
      currproduct.get_imgurl()
    with open(databasename, 'r+', newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in csvreader:
      if currproduct.pid not in row or currproduct.pid == "":
       currproduct.pid = currproduct.url.replace("https://www.target.com/p/","")
       nulist = currproduct.pid.split("/")
       currproduct.name = nulist[0]
       currproduct.pid = nulist[-1]
       currproduct.get_imgurl()
       f = open(databasetextname+"/"+currproduct.name+".txt","w")
       if( currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url is not None):
        f.write(currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url)
       f.close() 
       continue
      else:
       f = open(databasetextname+"/"+currproduct.name+".txt","r")
       
       previousstateofproduct.inStock = ("True" in f.read())
       f.close()
       if(previousstateofproduct.inStock == True and currproduct.get_stock() == False):
        outofstockalert(currproduct)
        f = open(databasetextname+"/"+currproduct.name+".txt","w")
        if( currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url is not None):
         f.write(currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url)
        f.close() 
        indatabase = True
       if(previousstateofproduct.inStock == False and currproduct.get_stock() == True):
        instockalert(currproduct)
        f = open(databasetextname+"/"+currproduct.name+".txt","w")
        if( currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url is not None):
         f.write(currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url)
        f.close()       
        indatabase = True
       if("False" in row and currproduct.inStock == True):
        instockalert(currproduct)
        f = open(databasetextname+"/"+currproduct.name+".txt","w")
        if( currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url is not None):
         f.write(currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url)
        f.close()       
        indatabase = False#updatedb(row,currproduct,csvfile)
        continue
       if("True" in row and currproduct.inStock == False):
        outofstockalert(currproduct)
        print("This condition was met")
        f = open(databasetextname+"/"+currproduct.name+".txt","w")
        if( currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url is not None):
         f.write(currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url)
        f.close()
        indatabase = False#updatedb(row,currproduct,csvfile)
       
        continue
       for cell in row:
        print(cell)
        try:
         fc = float(cell)
         if(fc > float(currproduct.price)):
          pricedecreasealert(currproduct)
          f = open(databasetextname+"/"+currproduct.name+".txt","w")
          if( currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url is not None):
           f.write(currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url)
          f.close()
          indatabase = False#updatedb(row,currproduct,csvfile)
         if(fc < float(currproduct.price)):
          priceincreasealert(currproduct)
          f = open(databasetextname+"/"+currproduct.name+".txt","w")
          if( currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url is not None):
           f.write(currproduct.name+ " in stock ? "+str(currproduct.inStock)+" price "+ currproduct.get_price()+currproduct.pid+" imgurl: "+currproduct.imgurl+"  url: "+currproduct.url)
          f.close()
          indatabase = False#updatedb(row,currproduct,csvfile)  
        except:

         continue
    csvfile.close()
    if(indatabase == False and currproduct.name+".txt" not in os.listdir("tDatabase")):
     with open(databasename, 'a+', newline='') as csvfile: 
      csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
     
      csvwriter.writerow([currproduct.name, str(currproduct.inStock), currproduct.price,currproduct.pid,currproduct.imgurl,currproduct.url]) 
     csvfile.close()
     newproductalert(currproduct)
   else:
    continue
def updatedb(row,product,csvfie):
 with open(databasename, 'a+', newline='') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
 for a in csvreader:
   if (a == row):
    csvwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow([product.name, str(product.inStock), product.price,product.pid,product.imgurl,product.url])
    break
 csvfile.close() 
 return row

def newproductalert(product):
 discordmsg.send("new product found" + product.name +"  url : "+ product.url)
 

def instockalert(product):
 discordmsg.send( product.name +" is now in stock url : "+ product.url)
def outofstockalert(product):
 discordmsg.send(product.name +" is now out of stock url : "+ product.url)
def pricedecreasealert(product):
 discordmsg.send(product.name +" is now on sale   url : "+ product.url)
def priceincreasealert(product):
 discordmsg.send(product.name +" has increased price   url : "+ product.url)

while(1 == 1):
 compareindatabase("a")
