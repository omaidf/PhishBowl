import os
import sys
import json
import mechanize
import requests
import sys
from mechanize import Browser

with open('verified_online.json') as json_data:
    output = json.load(json_data)
    # print output[1]["url"]
    # print output[1]["target"]
    # print output[1]["details"][0]["country"]
    # print output[1]["details"][0]["ip_address"]
    # br = mechanize.Browser()
    # br.addheaders = [('User-agent', 'Firefox')]
    # br.set_handle_equiv(True)
    # br.set_handle_redirect(True)
    # br.set_handle_robots(False)
    # br.open(output[1]["url"])
    # print br.title()

for site in output:
    print site["url"]

# br2 = mechanize.Browser()
# br2.open("https://www.phishtank.com/view_phish_redirect.php?phish_id=4993065")
# print br2.title()
# print br2.response().info()
# print br2.response().geturl()
# print br2.response().get_all_header_names(normalize=True)
# #Look for 'Server' and 'X-Powered-By' in array
# #if exists add
# print br2.response().__getitem__('Server')



#id = phishing id
#url = phishing url
#target = phishing target

