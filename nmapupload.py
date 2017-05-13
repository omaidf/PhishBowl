import requests
import sys

ip = sys.argv[1]

filepath = ip + '.xml'
url = "http://127.0.0.1:8081/artifactory/phish/"+ip+"/"
print url
with open(filepath) as fh:
    mydata = fh.read()
    response = requests.put(url,
               params={'file': filepath}
                )