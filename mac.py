# MAC-ADDRESS
# MAC address REST API - to query which company the mac address belongs to
#!/usr/bin/env python

import requests
import sys
import json



def isMAC48Address(inputString):
  if inputString.count(":")!=5:
    return False
  for i in inputString.split(":"):
    for j in i:
        if j>"F" or (j<"A" and not j.isdigit()) or len(i)!=2:
            return False
  return True


#GET  https://api.macaddress.io/v1?apiKey=at_5e1qs18klkBuc1ZJoujHQJvwBOJLI&output=json&search=44:38:39:ff:ef:57

URL = "https://api.macaddress.io/v1"
apiKey='at_5e1qs18klkBuc1ZJoujHQJvwBOJLI'
output="json"
timeout=3
print URL



# main program
macaddress = raw_input("Enter your MAC address: ")
print macaddress
# ret = isMAC48Address(macaddress)
# print ret

PARAMS = {'apiKey':apiKey, 'output':output, 'search':macaddress }

try:

   resp = requests.get(url = URL, params = PARAMS, timeout=(timeout, timeout + 25))

except requests.exceptions.Timeout:
    print "Network timed out in trying to reach the server."
    sys.exit(1)

if resp:
    print('Success!')
else:
    print('An error has occurred.')

if resp.status_code != 200:
    # This means something went wrong.
    print('An error has occurred.', resp.status_code)

try:
    data = resp.json()
    company = data['vendorDetails']['companyName']
    # Print details.
    print "The company associated with MAC address " + macaddress + " is : " + company
except ValueError:
    # includes simplejson.decoder.JSONDecodeError
    print "Invalid JSON data received! Decoding of JSON has failed" # Throw JSON error.
except Exception as e:
    print "An exception has occured while parsing the JSON data, following are the details:\n %s" % str(e)




