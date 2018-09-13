import requests

http_proxy  = "https://91.189.131.114:43115"
https_proxy = "https://91.189.131.114:43115"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }
def pxy_request(url):
 global proxieDict
 response = ""
 r = requests.get(url, proxies=proxyDict)
 response = r.text
 if(not detect_invalid_response()):

  print(response) 
  return response
 else:
  get_new_proxy(url)  
def detect_invalid_response():
 return False
def get_new_proxy(url):
 
 #implement finding a new proxy
 pxy_request(url)

pxy_request("https://www.google.com")
