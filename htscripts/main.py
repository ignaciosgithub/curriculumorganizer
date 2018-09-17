from urllib.request import urlopen as uReq
import requests
import os
import bs4
from bs4 import BeautifulSoup as soup
import dryscrape
class category:
 categoryid = ""
 categoryname = ""
 def set_categoryid(categoryid,value):
  categoryid = value
 def set_categoryname(categoryname,value):
  categoryname = value
class Product:
 producturl = ""
 price = 0
 instock = False
 productid = ""

def find_product_urls(category):
 counter = 0 
 htmlarray = []
 possibleproducturls = []
 narrow = []
 searchurl = "https://www.target.com/p/sitemap_001.xml.gz"
 session = dryscrape.Session()
 session.visit(searchurl)
 response = session.body()
 htmlarray = response.split('"')
 for a in htmlarray:
  if("https://" in a):
   counter = counter + 1
   print(a) 
 print(counter)  
 
sports = category()
sports.set_categoryid("N-5xt85")
sports.set_categoryname("sports-outdoors-deals")
find_product_urls(sports)
