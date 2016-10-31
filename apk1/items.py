# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
class Apk1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    xpath_download=scrapy.Field()
    xpath_pagelink=scrapy.Field()
    link=scrapy.Field()
    url = scrapy.Field()
    md5 = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    pass

