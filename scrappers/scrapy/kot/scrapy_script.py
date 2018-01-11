# from twisted.internet import reactor
# from scrapy.crawler import Crawler
# from scrapy.settings import Settings
# from scrapy import log
# from spiders import opera_spider
# import schedule
# import time

# def scrap(opera_spider):
#     crawler = Crawler(Settings())
#     crawler.configure()
#     crawler.crawl(opera_spider)
#     crawler.start()
#     log.start()
#     reactor.run()

#schedule.every(5).minutes.do(scrap)
# schedule.every().hour.do(job)
# schedule.every(1).day.at("10:30").do(scrap)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

# while True:
#      schedule.run_pending()
#      time.sleep(1)

#scrap();
