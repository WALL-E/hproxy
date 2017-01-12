# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import ipaddress

from scrapy.exceptions import DropItem

class HproxyPipeline(object):
    def process_item(self, item, spider):
        ip = item["ip"]
        if isinstance(ip, unicode):
            ip = ip.decode("utf-8")
        try:
            ip_tmp = ipaddress.IPv4Address(ip)
            if ip_tmp.is_private or ip_tmp.is_reserved or ip_tmp.is_multicast:
                raise DropItem("illegal ipaddress in %s" % item)
        except ipaddress.AddressValueError, msg:
            raise DropItem("illegal ipaddress in %s" % item)
        port = item["port"]
        if port < 0 or port > 65545:
            raise DropItem("illegal port in %s" % item)
        return item
