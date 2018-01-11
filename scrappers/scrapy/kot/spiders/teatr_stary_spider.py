import scrapy
from scrapy.selector import HtmlXPathSelector
from ..items import ShowItem, TheatreItemLoader

#tytuł
#response.xpath('//a[@class="row item"]//div[@class="title"]//span/text()').extract()
#godzina
#response.xpath('//a[@class="row item"]//div[@class="title"]/text()').extract()
#data
#response.xpath('//div[@class="single-day-list"]//div[@class="day"]//div[@class="number"]').extract()

class TheatreSpider(scrapy.Spider):
    name = "teatr"
    allowed_domains = ["http://www.kinokika.pl/dk.php"]
    start_urls = [
        "http://www.kinokika.pl/dk.php"
]
    shows_list_xpath = '//div[@class="single-day-list"]'
    item_fields = {
        'title': './a[@class="row item"]//div[@class="title"]//span/text()',
        'time': './a[@class="row item"]//div[@class="title"]/text()',
        'date': './div[@class="day"]//div[@class="number"]/text()',


    }

    def parse(self, response):

        selector = HtmlXPathSelector(response)

        for show in selector.select(self.shows_list_xpath):
            loader = TheatreItemLoader(ShowItem(), selector=show)

            for field, xpath in self.item_fields.items():
                loader.add_xpath(field, xpath)
            yield loader.load_item()