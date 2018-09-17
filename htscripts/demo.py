from urllib.request import urlopen as uReq
import requests
import os
import bs4
from bs4 import BeautifulSoup as soup
class Product:
 producturl = ""
 price = 0
 stock = 0
product = Product()
product.producturl = "https://www.target.com/p/cybertronpc-clx-set-gxm7400t-gaming-pc-with-liquid-cooled-amd-ryzen-7-1700x-processor-dual-nvidia-geforce-gtx-1070-graphics-cards-in-sli-black-blue/-/A-52514676"
uClient = requests.get(product.producturl)
page_html = uClient.text
uClient.close()
page_soup = soup(page_html,"html.parser")
newlist = []
for a in page_html.split('"'):
 if('image' in a):
  print(a)
