import requests

#proxy = "61.233.25.166:80"
proxy = "197.210.187.46"
http_proxy  = "https://91.189.131.114:43115"
https_proxy = "https://91.189.131.114:43115"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

proxies = {"https":"https://%s" % proxy}
url = "https://httpbin.org/ip"
headers={'User-agent' : 'Mozilla/5.0'}


r = requests.get(url, proxies=proxyDict)



print (r.text)

#r = requests.get(url, headers=headers, proxies=proxyDict)
