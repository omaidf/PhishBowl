import nmap
import os
import sys
import requests
ip = sys.argv[1]


nm = nmap.PortScanner()
nm.scan(hosts=ip,arguments='-T4 -A -v')
print(nm.csv())
csvfile = nm.csv()
f = open('scan.csv','w')
f.write(csvfile)
url = "http://127.0.0.1:8081/artifactory/phish/"+ip+"/"+csvfile
print url
files = {'file': open(csvfile, 'rb')}
response = requests.put(url, files=files)