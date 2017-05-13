import os
import sys
import json
import mechanize
import requests
import sys
import jenkins
from mechanize import Browser

record = {}
username = "admin"
password = "password"

with open('verified_online.json') as json_data:
    output = json.load(json_data)
    for site in output:
        url = site["url"]
        target = site["target"]
        country = ["details"][0]["country"]
        ip = ["details"][0]["ip_address"]
        startbuild(burl,btarget,bcountry,bip)

def startbuild(site,target,country,ip):
    record = {
    'url':url,
    'target':target,
    'country':country,
    'ip':ip
    }
    uploadurl = "http://127.0.0.1:8081/artifactory/"+ip
    r = requests.put(uploadurl, data=record,auth=(username,password))
    #start jenkins build
    #send IP Address and URL parameters to Build
    job _url = "http://127.0.0.1:8080/job/Recon/buildWithParameters?ip="+ip+"&url="+url
    status = requests.get(job_url)