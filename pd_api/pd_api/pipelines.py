# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PdApiPipeline(object):
	def __init__(self):
		self.file = open('pandas_api.csv', 'w')

	def process_item(self, item, spider):
		self.file.write('{0},{1}\n'.format(item['title'],item['link']))
		return item
