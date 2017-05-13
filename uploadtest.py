import requests
import sys

ip = "googletest"

filepath = 'test' + '.xml'
url = "http://52.38.111.29:8081/artifactory/phish/"+ip+"/test.xml"
print url
files = {'file': open('test.xml', 'rb')}
response = requests.put(url, files=files)