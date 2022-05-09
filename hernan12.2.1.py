# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
#  http://py4e-data.dr-chuck.net/known_by_Fikret.html
#  http://py4e-data.dr-chuck.net/known_by_Kellan.html


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
contra = int(input('Enter Count: '))
pos = int(input("Enter Position: "))-1
count = 0
for i in range(contra):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup('a')
    url = tag[pos].get('href', None)
    name = tag[pos].contents[0]

    print('Retrieving: ',name)
