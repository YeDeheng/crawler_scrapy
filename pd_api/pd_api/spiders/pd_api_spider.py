import scrapy
import urlparse
from pd_api.items import PdApiItem

class PdApiSpider(scrapy.Spider):
	name = "pandas_api"
	allowed_domains = ["pandas.pydata.org"]
	start_urls = ["http://pandas.pydata.org/pandas-docs/stable/api.html"]

	def parse(self, response):
		if response.xpath("//table[@class='longtable docutils']/tbody/tr/td[1]") != []:
			for href in response.xpath("//table[@class='longtable docutils']/tbody/tr/td[1]/a/@href"):
				url = response.urljoin(href.extract())
				yield scrapy.Request(url, callback=self.parse_result)

	def parse_result(self, response):
		#for sel in response.xpath("//dl[@class='method' or @class='function' or @class='data' or @class='class' or @class='attribute']/dt"):
		for sel in response.xpath("//dl/dt"):
			item = PdApiItem()
			if sel.xpath("a[@class='headerlink']/@href") != []:
				item['title'] = sel.xpath("@id").extract().pop().strip() #full name
				# item['title'] = sel.xpath("tt[@class='descname']/text()").extract() #short name
				item['link'] = urlparse.urljoin(response.url, sel.xpath("a[@class='headerlink']/@href").extract().pop().strip())
				yield item