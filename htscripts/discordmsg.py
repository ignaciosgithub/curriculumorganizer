import sys
 
# web library
import http.client
  
def send( message ):
 
    # your webhook URL
    webhookurl = "https://discordapp.com/api/webhooks/451547896438063141/K_cwyhz6Hgnz4-Qf7J-K1PDrFQrB7uw7lYQRTm54FzDRKM1pkuY6EHwZvpwZkoCxk_hZ"
 
    # compile the form data (BOUNDARY can be anything)
    formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------:::BOUNDARY:::--"
  
    # get the connection and make the request
    connection = http.client.HTTPSConnection("discordapp.com")
    connection.request("POST", webhookurl, formdata, {
        'content-type': "multipart/form-data; boundary=----:::BOUNDARY:::",
        'cache-control': "no-cache",
        })
  
    # get the response
    response = connection.getresponse()
    result = response.read()
  
    # return back to the calling function with the result
    return result.decode("utf-8")
 
 
 
# send the messsage and print the response

