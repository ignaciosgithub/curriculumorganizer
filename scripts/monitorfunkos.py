import random
from urllib.request import urlopen as uReq
import requests
import os
import bs4
from bs4 import BeautifulSoup as soup
import csv
import dryscrape
import re
import discordmsg
import isitinstock
import discordtwo
import pxy

def changeprice(newprice,filee):
 counter = 0
 filecontents = []
 f = open("Funkodb"+"/"+filee,"r")
 filecontents = f.read().split()
 f.close()
 f = open("Funkodb"+"/"+filee,"w")
 for a in filecontents:
  try:
   float(a)
   f.write(newprice + " ")
  except:
   f.write(a+ " ")
 
 url = filee.replace("{slashhere}","/").replace(".txt","")
 discordmsg.send("price has been updated to: $"+newprice+" on "+ filee.replace("{slashhere}","/").replace(".txt",""))
 try:
  discordtwo.sendproppermesage(url,url.replace("https://www.target.com",""), newprice +" $\n "+"  __Stock: False__\n Site: Target ","update", newprice +" $\n "+"  __Stock: False__\n Site: Target ",url )
 except:
  pass
 f.close()
def get_price(url):
 
 url = url+".txt"


 if("https" not in url):
   return "invalid"
  
 uClient = requests.get(url)
 page_html = uClient.text
 uClient.close()
 newlist = []
 for a in page_html.split():
  if '"price":' in a:
   newlist.append(a)
   break
 for b in newlist:
  for c in b.split(":"):
   
    
   if '"priceType"' in c:
    c=c.replace('"','')
    c = c.replace("priceType","")
    c = c.replace(",","")
    c = c.replace("$","") 
    print(c)
    return c

def changestock(newvalue,filee):
 counter = 0
 filecontents = []
 f = open("Funkodb"+"/"+filee,"r")
 filecontents = f.read().split()
 f.close()
 f = open("Funkodb"+"/"+filee,"w")
 for a in filecontents:
  if a  == "True" or a == "False":
   f.write(str(newvalue)+" ") 
  else:
   f.write(a+" ")
 f.close()
 url = filee.replace("{slashhere}","/").replace(".txt","")
 discordmsg.send("stock has been updated to: "+str(newvalue).replace("True","in Stock").replace("False","Not available in stock :-(")+" on "+ filee.replace("{slashhere}","/").replace(".txt",""))
 try:
  discordtwo.sendproppermesage(url,url.replace("https://www.target.com",""), get_price(url) +" $\n "+"  __Stock: False__\n Site: Target ","update", get_price(url)  +" $\n "+"  __Stock: False__\n Site: Target ",url )
 except:
  pass

def explore():
 url = ""
 price = ""
 stock = False
 
 for a in os.listdir("Funkodb"):
  url = a.replace("{slashhere}","/").replace(".txt","")
  uClient = requests.get(url)
  page_html = uClient.text
  uClient.close()
  price = get_price(url)
  f = open("Funkodb"+"/"+a,"r")
  if(price == None):
   continue
  if(price not in f.read()):
   f.close()
   changeprice(price,a)
  try:
   f.close()
  except:
   pass
  stock =isitinstock.isitinstock(url,price)
  
  f = open("Funkodb"+"/"+a,"r")
  if(str(stock) not in f.read()): 
   print(stock)
   print("stock value for")
   f.seek(0) 
   print(f.read())
   f.close()
   changestock(stock,a)
  try:
   f.close()
  except:
   pass
while(1 == 1):
 explore()



