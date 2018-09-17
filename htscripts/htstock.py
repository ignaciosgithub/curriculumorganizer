import requests
def get_stock(url):
 headers = headers={'User-Agent':'Mozilla/5.0'}
 uClient = requests.get(url,headers=headers)
 page_html = uClient.text
 uClient.close()
 splat = page_html.split(">")
 for a in splat:
  if('<meta property="og:availability" content=' in a):
  
  
   if( "outofstock" in a.replace('<meta property="og:availability" content=','').replace('"',"").replace(" /","")):
    return False
   return True
print(get_stock("https://www.hottopic.com/product/funko-supernatural-pop-television-castiel-with-wings-vinyl-figure-hot-topic-exclusive/10198879.html"))
