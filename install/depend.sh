#!/bin/bash

role=`id -u`
if test $role -ne 0
then
    echo "运行脚本需要root权限"
    exit 1
fi

pip2.7 install Scrapy
pip2.7 install ScrapyMongoDB
pip2.7 install http://oerp142a4.bkt.clouddn.com/pymongo-3.4.0.tar.gz
pip2.7 install http://oerp142a4.bkt.clouddn.com/beautifulsoup4-4.5.3.tar.gz
pip2.7 install http://oerp142a4.bkt.clouddn.com/ipaddress-1.0.17.tar.gz
