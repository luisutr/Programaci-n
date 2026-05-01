from bs4 import BeautifulSoup
import requests
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def robot():
    redditFile = requests.get("http://jarroba.com")
    redditHtml = redditFile.text
    redditFile.close()
    soup = BeautifulSoup(redditHtml)
    redditAll = soup.find_all("a")
    for links in redditAll:
        print (links.get('href'))
        #robot(links.get('href'))

robot()
