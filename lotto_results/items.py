# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
from scrapy.item import Item, Field


class LottoResultsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lotto = Field()
    pass


def DateSerializer(value):
    return datetime.datetime.strptime(value, "%b %d %y")


class LottoItem(scrapy.Item):
    url = scrapy.Field()
    draw = scrapy.Field()
    winning_combination = scrapy.Field()
    winning_value = scrapy.Field()
    num_of_winners = scrapy.Field()
    draw_date = scrapy.Field()
