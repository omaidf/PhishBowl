import mechanize
import requests
import sys
from mechanize import Browser

site = sys.argv[1]

# def recon(site):

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_robots(False)
br.set_handle_refresh(True, max_time=1)
br.open(site)
print br.response().code #should be 200
print br.response().info()
print br.response().geturl()
print br.response().geturl()

r = requests.head(site,allow_redirects=True)
print r.url
# print br.title()
# print br.geturl()
# print br.info()