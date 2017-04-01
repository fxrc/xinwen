# -*- coding: utf-8 -*-
import scrapy
import re

class XinwenSpider(scrapy.Spider):
    name = "xinwen"
    allowed_domians=["xinhuanet.com"]
    start_urls = ['http://www.news.cn/']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                url = href

                yield scrapy.Request(url,callback=self.parse_xinwen)
            except:
                continue

    def parse_xinwen(self,response):
        Dict={}
        try:
            name=response.css('.main_tit').css('h1::text').extract()
            content = response.css('p::text').extract()

            if len(name):
                Dict['title']=re.sub('\s','',name[0])
                b=''
                for a in content:
                    b+=a
                Dict['content'] = re.sub('\s', '', b)
                Dict['url']=response.url
                yield Dict
        except:
            pass

    def parse_url(self,response):
        pass
