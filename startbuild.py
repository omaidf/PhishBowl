import os
import sys
import json
import mechanize
import requests
import sys
from mechanize import Browser
import time

record = {}
username = "admin"
password = "password"

def startbuild(site,target,country,ip):
    record = {
    'url':url,
    'target':target,
    'country':country,
    'ip':ip
    }
    uploadurl = "http://127.0.0.1:8081/artifactory/api/storage/phish/"+ip+"/?properties=target="+target+";country="+country+";ip="+ip
    r = requests.put(uploadurl, auth=(username,password))
    #start jenkins build
    #send IP Address and URL parameters to Build
    job_url = "http://127.0.0.1:8080/job/Recon/buildWithParameters?ip="+ip+"&url="+url
    status = requests.get(job_url)
    time.sleep(5) # delays for 5 seconds

with open('verified_online.json') as json_data:
    output = json.load(json_data)
    for site in output:
        url = site["url"]
        target = site["target"]
        country = site["details"][0]["country"]
        ip = site["details"][0]["ip_address"]
        startbuild(url,target,country,ip)

