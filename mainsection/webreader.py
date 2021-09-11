from bs4 import BeautifulSoup
import requests

pagetoindex = 'https://www.redfin.com/city/3105/NC/Charlotte'
specificpage = 'https://www.zillow.com/charlotte-nc/'

page = requests.get(specificpage)
soup = BeautifulSoup(page.text, 'lxml')

houseprices = soup.find('div', attrs={'class':'bottomV2 '})
print(houseprices)
print(soup.prettify())
# the redfin system kicks out bots :(
# so does redfin 