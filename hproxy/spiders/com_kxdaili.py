# -*- coding: utf-8 -*-
import scrapy

from bs4 import BeautifulSoup
from hproxy.items import HproxyItem
import time


class ComKxdailiSpider(scrapy.Spider):
    name = "com_kxdaili"
    allowed_domains = ["kxdaili.com"]
    start_urls = ['http://www.kxdaili.com/dailiip.html']

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.findAll('table')
        table = tables[0]
        for tr in table.findAll('tr')[1:]:
            item = HproxyItem()
            tds = tr.findAll('td')
            if len(tds) > 0:
                item["ip"] = tds[0].string
                item["port"] = int(tds[1].string)
                item["timestamp"] = int(time.time())
                yield item
