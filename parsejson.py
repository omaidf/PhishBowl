import os
import sys
import json
import mechanize
import requests
import sys
from mechanize import Browser


site_record = {}
with open('verified_online.json') as json_data:
    output = json.load(json_data)
    print output[1]["url"]
    print output[1]["target"]
    print output[1]["details"][0]["country"]
    print output[1]["details"][0]["ip_address"]
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Firefox')]
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_robots(False)

# for site in output:
#     print site["url"]

# br2 = mechanize.Browser()
# br2.open("https://www.phishtank.com/view_phish_redirect.php?phish_id=4993065")


# print "Title is ",br2.title()
# br2.response().info()
# print "URL is " ,br2.response().geturl()

# headers = br2.response().get_all_header_names(normalize=True)

# if 'Server' in headers:
#     print br2.response().__getitem__('Server')

# if 'X-Powered-By' in headers:
#     print br2.response().__getitem__('X-Powered-By')


#Server Header
#X-Powered-By Headers
#IP Address
#Country
#Target
#Country
#Url


#nmap -T4 -A -v 127.0.0.1 -oX


#id = phishing id
#url = phishing url
#target = phishing target

