# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelSpiderItem(scrapy.Item):
    # define the fields for your item here like:
<<<<<<< HEAD
    name = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()
    address = scrapy.Field()
    content = scrapy.Field()
    site = scrapy.Field()
=======
    name = Field()
    title = Field()
    position = Field()
    date = Field()
    link = Field()
    category = Field()
    content = Field()
>>>>>>> 755bcf2f066b64f4c17eb26e4e42b80a21aa12ff
    pass
