import requests
import sys

ip = sys.argv[1]

filepath = ip + '.xml'
url = "http://127.0.0.1:8081/artifactory/phish/"+ip+"/"+filepath
print url
files = {'file': open(filepath, 'rb')}
response = requests.put(url, files=files)