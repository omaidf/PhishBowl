import requests
import sys

site_record = {}
username = "admin"
password = "password"


ip = "Apache"
xpow = "PHP"
title = "Google"
serv = "Server"
uploadurl = "http://52.38.111.29:8081/artifactory/api/storage/phish/"+ip+"?properties=Server="+serv+"|X-Powered-By="+xpow+"|title="+title
print uploadurl
r = requests.put(uploadurl,auth=(username,password))
