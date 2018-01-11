import scrapy
from scrapy.selector import HtmlXPathSelector
from ..items import ShowItem, ShowItemLoader


class OperaSpider(scrapy.Spider):
    name = "opera"
    allowed_domains = ["www.opera.krakow.pl"]
    start_urls = [
        "http://www.opera.krakow.pl/pl/repertuar/na-afiszu/listopad"


    ]

    shows_list_xpath = '//div[@class="row-fluid row-performance    "]'
    item_fields = {
        #'month':'.//ul[@class="nav nav-pills nav-repertuar"]/li[@class="active"]/a/text()',
        'title': './/h2[@class="item-title"]/a/text()',
        'time': './/div[@class="item-time vertical-center"]/div[@class="vcentered"]/text()',
        'date': './/div[@class="item-date vertical-center"]/div[@class="vcentered"]/text()',


    }




    def parse(self, response):

        selector = HtmlXPathSelector(response)

        for show in selector.select(self.shows_list_xpath):
            loader = ShowItemLoader(ShowItem(), selector=show)

            for field, xpath in self.item_fields.items():
                loader.add_xpath(field, xpath)
            yield loader.load_item()


        list = ["styczen", "luty"
            , "marzec", "kwiecien"
            , "maj", "czerwiec"
            , "lipiec", "sierpien"
            , "wrzesien", "pazdziernik"
            , "listopad", "grudzien"]

        for i in list:
            next_page = ("http://www.opera.krakow.pl/pl/repertuar/na-afiszu/%s" % i)
            yield scrapy.Request(next_page, callback=self.parse)

