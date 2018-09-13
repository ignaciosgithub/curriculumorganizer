from urllib.request import urlopen as uReq
import requests
import os
import bs4
from bs4 import BeautifulSoup as soup
import csv
import dryscrape
import re
import discordmsg
string = '"53621948":{"isNetworkDiscontinued":true,"isDiscontinued":true,"isNetworkOutOfStock":true,"isStoreOutOfStock":true,"isOutOfStock":true'
string2 = '"53621948":{"isNetworkDiscontinued":false,"isDiscontinued":false,"isNetworkOutOfStock":true,"isStoreOutOfStock":true,"isOutOfStock":true'
string3 = '"53621948":{"isNetworkDiscontinued":false,"isDiscontinued":true,"isNetworkOutOfStock":true,"isStoreOutOfStock":true,"isOutOfStock":true'
string4 = '"53621948":{"isNetworkDiscontinued":true,"isDiscontinued":false,"isNetworkOutOfStock":true,"isStoreOutOfStock":true,"isOutOfStock":true'


def isitinstock(url,z):
 idd = ""
 newarray = url.split("/")
 for a in newarray:
  if "A-" in a:
   idd = a.replace('A-',"")
 uClient = requests.get(url)
 page_html = uClient.text
 uClient.close()
 
 if(string.replace("53621948",idd) in page_html or string2.replace("53621948",idd) in page_html or string3.replace("53621948",idd) in page_html or string4.replace("53621948",idd) in page_html):
  return(False)
 else:
  return(True)
 

#print(isitinstock("https://www.target.com/p/funko-pop-games-destiny-ikora-mini-figure/-/A-52891798","53621948"))
# and '"@type":"Offer","price":"'+price+'","priceCurrency":"USD","availability":"OutOfStock","availableDeliveryMethod":"OnSitePickup","deliveryLeadTime"' not in page_html
#"53621948":{"isNetworkDiscontinued":true,"isDiscontinued":true,"isNetworkOutOfStock":true,"isStoreOutOfStock":true,"isOutOfStock":true,"isLoyaltyNetworkOutOfStock":true,"isLoyaltyOutOfStock":true,
