import requests

headers = headers={'User-Agent':'Mozilla/5.0'}
uClient = requests.get("https://www.hottopic.com/product/funko-kagamine-len-pop-rocks-vinyl-figure/10249781.html",headers=headers)
page_html = uClient.text
uClient.close()
splat = page_html.split(">")
price = 0
for a in splat:
 if('image' in a):
  
  
  print(a)
