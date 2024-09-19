import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dhooks import Webhook, Embed
from threading import Thread
import random
import time

def webhook(sku, title, img, qty, status):
	#link = "https://www.ebay.com/itm/{}".format(sku)
	link = product_dict[sku]
	hook = Webhook('https://discordapp.com/api/webhooks/722879574819471461/j1t1k3XRDQ_E_99DCewt76k0e3HdIxqZYQoZQp0kI2ceFIi6r8PjhxusfI16fRJEDhlo')
	color_list = [0xE53238, 0x0064D2, 0xF5AF02, 0x86B817]
	embed = Embed(
	description="[Add to Cart](" + link + ")",
	#color=0x1ab83c,
	color=random.choice(color_list),
	timestamp='now'
	)

	embed.set_author(name=title, icon_url=None, url=link)
	#embed.add_field(name='Store:', value=name, inline=True)
	embed.add_field(name='Status:', value=status, inline=True)
	embed.add_field(name='Availability:', value=str(qty), inline=True)

	embed.set_footer(text='created by enrique#2519', icon_url='https://cdn.discordapp.com/avatars/267782036893204481/58904351e4e12eec9302b22cd6b209d9.webp?size=256')

	embed.set_thumbnail(img)
	#embed.set_image(image2)

	try:
		hook.send(embed=embed)
		#print('Webhook sent')
	except Exception as e:
		print('Webhook failed: {}'.format(e))

def monitor(sku):
	page = requests.get('https://www.ebay.com/itm/{}'.format(sku))
	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find('title').text
	if title.endswith('| eBay'):
		title = title[:-7]
		title = title.split(' ')
		title.pop(-1)
		title = ' '.join(title)
	images = soup.find_all('img')

	src = None

	for img in images:
		if "https://i.ebayimg.com/images/" in img['src']:
			src = img['src']
			break

	qty = soup.find("span", class_="qtyTxt").text.split()
	qty = ' '.join(qty).split(' / ')[0]

	atc_button = soup.find(id="atcRedesignId_btn")
	if atc_button != None:
		atc_button = atc_button.text
		status = ' '.join(atc_button.split())
		webhook(sku, title, src, qty, status)
	else:
		status = "Out of Stock"
	#webhook(sku, title, src, qty, status)

	print('eBay [{}]\t[{}]\t{}'.format(datetime.now().strftime('%m-%d %H:%M:%S'), sku, status))
	

def run(sku):
	while True:
		monitor(sku)
		time.sleep(20)

if __name__ == '__main__':
	product_dict = {
	353088064614 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353088064614',
	233461932932 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233461932932',
	#303579326612 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F303579326612', # [Unavailable] Intex Easy Set 18ft
	391685377035 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F391685377035',
	392633533047 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F392633533047',
	353088063415 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353088063415',
	353088042569 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F353088042569',
	233596044434 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233596044434',
	#233600592615 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233600592615',
	392814290351 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F392814290351',
	#392806818717 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F392806818717',
	233461227027 : 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575598825&toolid=10001&campid=5338702441&customid=pool&mpre=https%3A%2F%2Fwww.ebay.com%2Fitm%2F233461227027',
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

	print("""\
███████╗███╗   ██╗██████╗ ██╗ ██████╗ ██╗   ██╗███████╗
██╔════╝████╗  ██║██╔══██╗██║██╔═══██╗██║   ██║██╔════╝
█████╗  ██╔██╗ ██║██████╔╝██║██║   ██║██║   ██║█████╗  
██╔══╝  ██║╚██╗██║██╔══██╗██║██║▄▄ ██║██║   ██║██╔══╝  
███████╗██║ ╚████║██║  ██║██║╚██████╔╝╚██████╔╝███████╗
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝ 
                                                       """)
	print("*** eBay Monitor v.1.1.4 ***\n")
	loop = input("Press any key to start...")

	for product in raw_ids:
		t = Thread(target=run, args=(product,))
		t.start()
		print('[{}]\tThread Started: {}'.format(datetime.now().strftime('%m-%d %H:%M:%S'), product))
		time.sleep(2.0)
