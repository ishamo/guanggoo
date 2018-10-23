# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from guanggoo.items import PostItem


class PostSpider(CrawlSpider):
    name = 'post'
    allowed_domains = ['www.guanggoo.com']
    start_urls = ['http://www.guanggoo.com/']

    rules = (
        Rule(LinkExtractor(allow='/t/[0-9]+'), follow=True, callback='parse_item'),
        Rule(LinkExtractor(allow='\?p=[0-9]+'))
    )

    def parse_item(self, response):
        url = response.url
        title = response.xpath('//h3[@class="title"]/text()').extract_first()
        content = response.xpath('//div[@class="ui-content"]/p/text()').extract_first()
        p = PostItem(url=url, title=title, content=content)
        yield p
