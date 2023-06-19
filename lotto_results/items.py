# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class LottoResultsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lotto = Field()
    pass


class LottoItem(scrapy.item):
    url = scrapy.Field()
    draw = scrapy.Field()
    winning_combination = scrapy.Field()
    winning_value = scrapy.Field()
    draw_date = scrapy.Field()
