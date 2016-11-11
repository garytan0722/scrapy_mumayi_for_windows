# -*- coding: utf-8 -*-

import json
import base64
from scrapy_splash import SplashRequest
import scrapy
from apk1.items import Apk1Item
class apkspider(scrapy.Spider):
    def __init__(self, category='',start=None, end=None, *args, **kwargs):
        super(apkspider, self).__init__(*args, **kwargs)
        start_int=int(start)
        end_int=int(end)
        for i in range(start_int,end_int):#451
            self.link="http://www.mumayi.com/android/zhutibizhi/list_8_%i.html" %i
            self.start_urls.append(self.link)
        print ("START_URL:")
        print(self.start_urls)
    download_delay=2
    name = "mumayi"
    allowed_domains = ["down.mumayi.com","www.mumayi.com"]
    #start_urls = ["http://www.mumayi.com/android-18.html"]
    #for i in range(351,451):#1114
        #link="http://www.mumayi.com/android/zhutibizhi/list_8_%i.html" %i
        #start_urls.append(link)
    #print ("START_URL:")
    #print(start_urls)
    def parse(self, response):
        xpath_pagelink=response.xpath('//a[@class="img72_72"]/@href').extract()
        print ("HREF:")
        print(xpath_pagelink)
        for i in range(len(xpath_pagelink)):
            url=xpath_pagelink[i]
            print("URL:"+url)
            yield scrapy.Request(url, callback=self.parseforlink)
    def parseforlink(self,response):
        xpath_download=response.xpath('//a[@class="download fl"]/@href').extract()
        #print (response.body)
        print (xpath_download)
        yield scrapy.Request(xpath_download[0], callback=self.download)
    def download(self, response):
        link=response.url
        print("APK FILE DST:"+link)
        myitem = Apk1Item()
        myitem["file_urls"]=[link]
        yield myitem

     