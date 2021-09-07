from bs4 import BeautifulSoup
import urllib2

pagetoindex = 'https://www.redfin.com/city/3105/NC/Charlotte'

with open(pagetoindex) as fp:
    soup = BeautifulSoup(fp, 'lxml')

print(soup.prettify())