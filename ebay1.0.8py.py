import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dhooks import Webhook, Embed
from threading import Thread
import random
import time

def webhook(sku, title, img, qty, status):
	link = "https://www.ebay.com/itm/{}".format(sku)
	hook = Webhook('https://discordapp.com/api/webhooks/722221372486451247/1RN7GKfEopKSJIajBz4uGONaYPTlzGQqe0GxG5Ov9pfRP_4bbGaCJhFZ7c3kcuG0tVxQ')
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

	print('[{}]\t[{}]\t{}'.format(datetime.now().strftime('%m-%d %H:%M:%S'), sku, status))
	

def run(sku):
	while True:
		monitor(sku)
		time.sleep(60)

if __name__ == '__main__':
	products = [
	353088064614,
	233461932932,
	303579326612
	]

	print("""\
███████╗███╗   ██╗██████╗ ██╗ ██████╗ ██╗   ██╗███████╗
██╔════╝████╗  ██║██╔══██╗██║██╔═══██╗██║   ██║██╔════╝
█████╗  ██╔██╗ ██║██████╔╝██║██║   ██║██║   ██║█████╗  
██╔══╝  ██║╚██╗██║██╔══██╗██║██║▄▄ ██║██║   ██║██╔══╝  
███████╗██║ ╚████║██║  ██║██║╚██████╔╝╚██████╔╝███████╗
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝ 
                                                       """)
	print("*** eBay Monitor v.1.0.0 ***\n")
	loop = input("Press any key to start...")

	for product in products:
		t = Thread(target=run, args=(product,))
		t.start()
		print('[{}]Thread Started: {}'.format(datetime.now().strftime('%m-%d %H:%M:%S'), product))
		time.sleep(3.0)
