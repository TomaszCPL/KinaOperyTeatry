import scrapy
from ..items import ShowItem, KikaItemLoader
from scrapy.selector import HtmlXPathSelector

class KikaSpider(scrapy.Spider):
    name = "kika"
    allowed_domains = ["http://www.kinokika.pl/dk.php"]
    start_urls = [
        "http://www.kinokika.pl/dk.php"
]
    shows_list_xpath = '//b'
    item_fields = {
        'title': './text()',
        'time': './preceding-sibling::small[1]/text()',
        'date': './ancestor::ul[1]/preceding-sibling::h2[1]/text()',


    }

    def parse(self, response):

        selector = HtmlXPathSelector(response)

        for show in selector.select(self.shows_list_xpath):
            loader = KikaItemLoader(ShowItem(), selector=show)

            for field, xpath in self.item_fields.items():
                loader.add_xpath(field, xpath)
            yield loader.load_item()



#SECOND VERSION
# class KikaSpider(scrapy.Spider):
#     name = "kika"
#     allowed_domains = ["http://www.kinokika.pl/dk.php"]
#     start_urls = [
#         "http://www.kinokika.pl/dk.php"
#
#
#     ]
#     def parse(self, response):
#         divs = list(response.xpath("//b"))
#         #l = KikaItemLoader(item=KikaItem(), response=response)
#         print(divs)
#         for div in divs:
#             l = KikaItemLoader(item=KikaItem(), response=div),
#             l.add_xpath("title", './text()'),
#             l.add_xpath("date", "./ancestor::ul[1]/preceding-sibling::h2[1]/text()"),
#             l.add_xpath("time", "./preceding-sibling::small[1]/text()"),
#             return l.load_item()
