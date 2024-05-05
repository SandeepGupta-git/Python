import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # for access html contents from secure web.
# ignore ssl certificate errors
contexts = ssl.create_default_context()
contexts.check_hostname = False
contexts.verify_mode = ssl.CERT_NONE
url = input('Enter any URL -')

html = urllib.request.urlopen(url,context=contexts).read()
soup = BeautifulSoup(html, 'html.parser')

count = dict()
totalhref = 0
#retrive all a tag

tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) # print all hrefs
    totalhref = totalhref + 1    
    count[tag] = count.get(tag, 0) + 1
print('count' , count) # number of occurance of each href
print('Total Href', totalhref) # total number of href in that web page
