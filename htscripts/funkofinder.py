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
import time
delayfile = open("config.txt","r")
delaytext = delayfile.read().replace("Sleep=","")

alltargetdbs = ["https://www.target.com/p/sitemap_001.xml.gz","https://www.target.com/p/sitemap_002.xml.gz","https://www.target.com/p/sitemap_003.xml.gz","https://www.target.com/p/sitemap_004.xml.gz","https://www.target.com/p/sitemap_005.xml.gz","https://www.target.com/p/sitemap_006.xml.gz","https://www.target.com/p/sitemap_007.xml.gz""https://www.target.com/p/sitemap_008.xml.gz","https://www.target.com/p/sitemap_009.xml.gz","https://www.target.com/p/sitemap_010.xml.gz","https://www.target.com/p/sitemap_011.xml.gz","https://www.target.com/p/sitemap_012.xml.gz","https://www.target.com/p/sitemap_013.xml.gz","https://www.target.com/p/sitemap_014.xml.gz","https://www.target.com/p/sitemap_015.xml.gz","https://www.target.com/p/sitemap_016.xml.gz","https://www.target.com/p/sitemap_017.xml.gz","https://www.target.com/p/sitemap_018.xml.gz","https://www.target.com/p/sitemap_019.xml.gz"]
#discordmsg.send("funko specific target monitor started")
def get_id(url):
 a = url.split("/")
 for b in a:
  if "A-" in b:
   return b.replace("A-","")


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
   return isitinstock.isitinstock(self.url,self.get_price())
  except:
   return False  
 def get_price(self):
  if("https" not in self.url):
   return "invalid"
  
  uClient = requests.get(self.url)
  page_html = uClient.text
  uClient.close()
  newlist = []
  for a in page_html.split():
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
 try:
  uClient = pxy.pxy_request(databaseurl)
  page_html = uClient
 except: 
  uClient = requests.get(databaseurl)
  page_html = uClient.text
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
  f.write(funkodoll.url + " Price " + funkodoll.price + " stockstate = "+str(funkodoll.inStock) )
  f.close()
  discordtwo.sendproppermesage(funkodell.url,funkodoll.url.replace("https://www.target.com",""), get_price(funkodoll.url) +" $\n "+"  __Stock: False__\n Site: Target ","update price", get_price(funkodoll.url) +" $\n "+"  __Stock: "+ get_stock(funkodoll.url)+"\n Site: Target ","https://target.scene7.com/is/image/Target/" + str(get_id(funkodoll.url)) )
for b in alltargetdbs:
 a = findfunkos(b)
 print("starting to save")
 for i in a:
  funkocontainer.url = i
  funkocontainer.get_price()
  funkocontainer.get_stock()
  savefunko(funkocontainer)






