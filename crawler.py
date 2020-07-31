import requests
from parsel import Selector

import time
start = time.time()

### Crawling to the website
response = requests.get('http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=2&RegionName=Aurangabad')

## Setup for scrapping tool

selector = Selector(response.text)

# Extracting href attribute from anchor tag <a href="*">
href_links = selector.xpath('//a/@href').getall()


print('*****************************href_links************************************')
print(href_links)
print('*****************************/href_links************************************')



end = time.time()
print("Time taken in seconds : ", (end-start))