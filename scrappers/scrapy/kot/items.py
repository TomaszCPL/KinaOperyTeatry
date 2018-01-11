# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import re

import scrapy
from scrapy.contrib.loader import ItemLoader
from scrapy.loader.processors import Join, MapCompose, TakeFirst


#
# def replace_whitespace(y):
#     return y.translate(None," \n\t\r")


class ShowItem(scrapy.Item):
    place = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    date = scrapy.Field()
    #place = scrapy.Field()

class KikaItem(scrapy.Item):
    place = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    date = scrapy.Field()
    #place = scrapy.Field()

def strip_string(x):
    return x.strip()
#
def replace_whitespace(x):
    return x.replace(" ","")

def lowercase(x):
    return x.lower()

def match_date(string):
    regex=re.findall(r'(0?[1-9]|[12][0-9]|3[01])[\/\-\.](0?[1-9]|1[012])[\/\-\.]\d{4}',string)
    return regex

def kkk(x):
    return x.join()

class ShowItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(strip_string,lowercase)
    title_out = Join()

    month_in = MapCompose(strip_string)
    month_out = Join()

    time_in = MapCompose(strip_string)
    time_out = Join()

    date_in = MapCompose(strip_string)
    date_out = Join('')
    #date_in = MapCompose(replace_whitespace)
    #date_out = MapCompose(match_date)

class KikaItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(strip_string,lowercase)
    title_out = Join()

    month_in = MapCompose(strip_string)
    month_out = Join()

    time_in = MapCompose(strip_string)
    time_out = Join()

    date_in = MapCompose(strip_string)
    date_out = Join('')
    #date_in = MapCompose(replace_whitespace)
    #date_out = MapCompose(match_date)

class TheatreItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(strip_string,lowercase)
    title_out = Join()

    month_in = MapCompose(strip_string)
    month_out = Join()

    time_in = MapCompose(strip_string)
    time_out = Join()

    date_in = MapCompose(strip_string)
    date_out = Join('')
    #date_in = MapCompose(replace_whitespace)
    #date_out = MapCompose(match_date)

