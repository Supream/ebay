import requests
from bs4 import BeautifulSoup

product_dict = {
353088064614 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353088064614',
233461932932 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233461932932',
#303579326612 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F303579326612', # [Unavailable] Intex Easy Set 18ft
391685377035 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F391685377035',
392633533047 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F392633533047',
353088063415 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353088063415',
353088042569 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353088042569',
#233596044434 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233596044434',
353099774129 : 'http://ebay.com/itm/353099774129',
233617635669 : 'http://ebay.com/itm/233617635669',
353084109712 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353084109712',
#233600592615 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233600592615',
392814290351 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F392814290351',
#392806818717 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F392806818717',
#233461227027 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233461227027', # Filter 28635EG
392806745301 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F392806745301',
#233596042642 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233596042642',
353088046421 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353088046421',
233600588369 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233600588369',
353103974065 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353103974065',
233600593732 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233600593732',
233594262980 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233594262980',
233461227027 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233461227027',
303579317409 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F303579317409',
233624041899 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233624041899'
}

raw_ids = list(product_dict.keys())


with open("links.txt", "a") as f:
	for sku in raw_ids:
		page = requests.get('https://www.ebay.com/itm/{}'.format(sku))
		soup = BeautifulSoup(page.content, 'html.parser')

		title = soup.find('title').text
		print('{}\t{}'.format(sku, title), file=f)

