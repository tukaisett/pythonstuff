# nwinners_list_spider.py
import scrapy
import re

BASE_URL = 'http://en.wikipedia.org'
# ...
def process_winner_li(w, country=None):
	"""
	Process a winner's <li> tag, adding country of birth or
	nationality, as applicable.
	"""
	wdata = {}
	wdata['link'] = BASE_URL + w.xpath('a/@href').extract()[0]
	text = ' '.join(w.xpath('descendant-or-self::text()')
		.extract())
	# get comma-delineated name and strip trailing whitespace
	wdata['name'] = text.split(',')[0].strip()

	year = re.findall('\d{4}', text)
	if year:
		wdata['year'] = int(year[0])
	else:
		wdata['year'] = 0
		print('Oops, no year in ', text)
	category = re.findall(
			'Physics|Chemistry|Physiology or Medicine|Literature|'\
			'Peace|Economics',
				text)
	if category:
		wdata['category'] = category[0]
	else:
		wdata['category'] = ''
		print('Oops, no category in ', text)
	
	if country:
		if text.find('*') !=-1:
			wdata['country'] = ''
			wdata['born_in'] = country
		else:
			wdata['country'] = country
			wdata['born_in'] = ''

	# store a copy of the link's text string
	# for any manual corrections
	wdata['text'] = text
	return wdata

# A. Define the data to be scraped
class NWinnerItem(scrapy.Item):
	country = scrapy.Field()
	name = scrapy.Field()
	link_text = scrapy.Field()

# B Create a named spider
class NWinnerSpider(scrapy.Spider):
	""" Scrapes the country and link text of the Nobel-winners. """
	name = 'nwinners_list'
	allowed_domains = ['en.wikipedia.org']
	start_urls = [
		"https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country"
	]
	# C A parse method to deal with the HTTP response
	def parse(self, response):
		h2s = response.xpath('//h2')
		h2s = h2s[3:]
		for h2 in h2s:
			country = h2.xpath('span[@class="mw-headline"]/text()').extract()
			if country:
				winners = h2.xpath('following-sibling::ol[1]')
				for w in winners.xpath('li'):
					text = w.xpath('descendant-or-self::text()').extract()
					#wdata = process_winner_li(w, country[0])
					yield NWinnerItem(
						country=country[0], name=text[0],
						link_text = ' '.join(text)
						)


