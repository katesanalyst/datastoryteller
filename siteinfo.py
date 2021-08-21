'''
This is extract the SITE links for information purpose; which was developed both request_HTML and BS4; However, both works extremly one after another.
it will be educational purpose and to know about site work flow and may  find more data further...
currentnly, integrated and  excuted  either requestsHTML or BS4; when requestsHTML faild to retrive link then BS4 will take a call ;)
still in my mind supports requestHTML

'''

import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from urllib.parse import urljoin


url = 'https://www.jiomart.com/'

session = HTMLSession()
response = session.get(url); ls = []
for re in response.html.find('a'):
    if re.absolute_links is not ls:
        ls.append(''.join(re.absolute_links))
if (len(ls) == 0):
    x = requests.get(url)
    soup = BeautifulSoup(x.text,features='lxml')
    for sa in soup.find_all('a'):
        if sa.attrs['href'] is not ls:
            ls.append(urljoin(x.url,sa.attrs['href']))
    print("This is BS4 [%s]:\n %s" %(len(ls),ls))
else:
    print ("This is requestsHTML [%s]:\n %s" %(len(ls),ls))



