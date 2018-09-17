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
import time
import htstock
#https://target.scene7.com/is/image/Target/53621948

delayfile = open("config.txt","r")
delaytext = delayfile.read().replace("Sleep=","")

def get_id(url):
 
 a = url.split("/")
 for b in a:
  if(".html" in b):
   return b.replace(".html","").replace(".txt","")
  
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

 
 discordtwo.sendproppermesage(url,url.replace("https://www.hottopic.com/product/",""), get_price(url) +" $\n "+"  __Stock: False__\n Site: HotTopic ","Price update ",  get_price(url)+ " $\n "+"  __Stock: "+str(htstock.get_stock(url))+"\n Site: HotTopic ","https://hottopic.scene7.com/is/image/HotTopic/"+str(int(get_id(url))-1)+"_hi",fields=["test1","test2"])

 f.close()
def get_price(url):
 
 url = url


 if("https" not in url):
   return "invalid"
 
 headers={'User-Agent':'Mozilla/5.0'}
 uClient = requests.get(url,headers=headers)
 page_html = uClient.text
 uClient.close()
 newlist = []
 for a in page_html.split(">"):
  if '<meta property="product:price:amount" content=' in a:
   return a.replace('<meta property="product:price:amount" content=',"").replace("/","").replace('"',"").replace(" ","")

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
 #discordmsg.send("stock has been updated to: "+str(newvalue).replace("True","in Stock").replace("False","Not available in stock :-(")+" on "+ filee.replace("{slashhere}","/").replace(".txt",""))
 
 discordtwo.sendproppermesage(url,url.replace("https://www.hottopic.com/product/",""), get_price(url) +" $\n "+"  __Stock: False__\n Site: HotTopic ","Stock update ",  get_price(url)+ " $\n "+"  __Stock: "+str(newvalue)+"\n Site: HotTopic ","https://hottopic.scene7.com/is/image/HotTopic/"+str(int(get_id(url))-1)+"_hi",fields=["test1","test2"])


 

def explore():
 url = ""
 price = ""
 stock = False
 print("i am exploring")
 for a in os.listdir("Funkodb"):
  
  global delaytext 
  time.sleep(int(delaytext))  
  url = a.replace("{slashhere}","/").replace(".txt","")
  
  uClient = requests.get(url)
  page_html = uClient.text
  uClient.close()
  price = get_price(url)
  
  print(price)
  
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
  try:
   stock = htstock.get_stock(url)
  except:
   print("returning")
   return
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

