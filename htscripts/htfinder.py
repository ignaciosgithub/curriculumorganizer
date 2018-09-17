from urllib.request import urlopen as uReq
import requests
import os
import bs4
from bs4 import BeautifulSoup as soup
import csv
import dryscrape
import re
import discordtwo
import isitinstock
import time
import discordmsg
import htstock
delayfile = open("config.txt","r")
delaytext = delayfile.read().replace("Sleep=","")

alltargetdbs = ["https://www.hottopic.com/sitemap_0.xml","https://www.hottopic.com/sitemap_1.xml"]
#discordmsg.send("funko specific target monitor started")
def get_id(url):
 a = url.split("/")
 for b in a:
  if ".html" in b:
   print(b)
   return int(b.replace(".html",""))


def check_keywords(info):
 f = open("keywords.txt","r")
 for a in f.read().split(","):
  f.seek(0)
  
  if a in info:
  
   f.close()
   return True
 f.close() 
 return False

class Funkodoll:
 inStock = False
 price = ""
 url = ""
 def get_stock(self):
  global delaytext 
  time.sleep(int(delaytext))
  try: 
   return htstock.get_stock(self.url)
  except:
   return False  
 def get_price(self):
  if("https" not in self.url):
   return "invalid"
  headers={'User-Agent':'Mozilla/5.0'}
  uClient = requests.get(self.url,headers=headers)
  page_html = uClient.text
  uClient.close()
  newlist = []
  for a in page_html.split(">"):
   if '<meta property="product:price:amount" content=' in a:
    return a.replace('<meta property="product:price:amount" content=',"").replace("/","").replace('"',"").replace(" ","")

     
funkocontainer = Funkodoll()
a = []
def findfunkos(databaseurl):
 dirtyurls = []
 funkourls = []
 tosearch = databaseurl
 global delaytext 
 time.sleep(int(delaytext)) 
 

 headers={'User-Agent':'Mozilla/5.0'} 
 uClient = requests.get(databaseurl,headers=headers)
 page_html = uClient.text
 uClient.close()
 print(page_html)
 for a in page_html.split('\n'):
  if("<loc>" in a and "</loc>"):
    dirtyurls.append(a.replace('<loc>','').replace('</loc>',''))
 for c in dirtyurls:
  if (True == check_keywords(c)):
    funkourls.append(c)
 return funkourls






def showfunkos(funkourls):
 print(funkourls)
def savefunko(funkodoll):
 print(os.path.isfile("Funkodb/"+funkodoll.url.replace(" ","").replace("/","{slashhere}")+".txt"))
 if(False == (os.path.isfile("Funkodb/"+funkodoll.url.replace(" ","").replace("/","{slashhere}")+".txt"))):
  f = open("Funkodb/"+funkodoll.url.replace(" ","").replace("/","{slashhere}")+".txt","w")
  f.write(funkodoll.url + " Price " + funkodoll.get_price() + " stockstate = "+str(funkodoll.get_stock()) )
  f.close()
  print(funkodoll.url)
  discordmsg.send("new hot topic product found")
  
  discordtwo.sendproppermesage(funkodoll.url,funkodoll.url.replace("https://www.hottopic.com/product/",""), funkodoll.get_price() +" $\n "+"  __Stock: False__\n Site: HotTopic ","New hot topic product found",  funkodoll.get_price()+ " $\n "+"  __Stock: "+str(funkodoll.get_stock())+"\n Site: HotTopic ","https://hottopic.scene7.com/is/image/HotTopic/"+str(get_id(funkodoll.url)-1)+"_hi",fields=["test1","test2"])
for b in alltargetdbs:
 a = findfunkos(b)
 print("starting to save")
 for i in a:
  funkocontainer.url = i
  funkocontainer.get_price()
  funkocontainer.get_stock()
  savefunko(funkocontainer)
