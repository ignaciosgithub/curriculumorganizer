import requests
import random
http_proxy  = "https://103.14.36.36:59937"
https_proxy = "https://103.14.36.36:59937"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }
def pxy_request(url):
 global proxieDict
 proxyfile = open("proxylist.txt","r")
 proxylist = proxyfile.read().split()
 global http_proxy
 global https_proxy
 ch = random.choice(proxylist)
 http_proxy = "https://"+ch
 https_proxy = "https://"+ch
 proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }
 
 response = ""
 r = requests.get(url, proxies=proxyDict)
 response = r.text
 r.close()
 if(not detect_invalid_response()):

   
  return response
 else:
  get_new_proxy(url)  
def detect_invalid_response():
 return False
def get_new_proxy(url):
 
 #implement finding a new proxy
 pxy_request(url)


