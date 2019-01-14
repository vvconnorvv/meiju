# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'  # 爬虫名。 一个项目下可能有多个爬虫，并且每个爬虫有优先级，并发等设置。 scrapy crawl [spider_name]
    allowed_domains = ['meijutt.com']  # 为了防止爬虫项目自动爬去到其他网站，设置限制，每一次请求前都会检查请求的网址是否属于这个域名下，是的话才允许请求。注意：爬取日志爬取网址后响应总为None，检查allowed_domain书写是否正确。值是一级域名。
    start_urls = ['https://www.meijutt.com/new100.html']  # 第一个请求的url，整个程序逻辑的入口。得到的response返回给self.parse(self, response=response)

    def parse(self, response):
        # print(response.status_code, response.content, response.text)
        # 非框架下写法 dom = lxml.etree.HTML(response.text); dom.xpath('')
        # scrapy框架下正规写法 Selector(response.text).xpath('').extract()

        # 获取剧集名
        movie_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')  # [<li>对象, <li>对象,>]

        for movie in movie_list:
            # xpath()返回[Selector(), Selector()] 功能强，可以在selector对象上进行第二次解析
            # xpath().extract()返回['剧集名1','剧集名2','...']，打印或debug时看着清楚
            # xpath().extract_first() 返回'剧集名1' 只返回第一个
            # .表示在子标签基础上继续解析
            name = movie.xpath('./h5/a/text()').extract_first()
            # fenlei= movie.xpath('./span[@class="mjjq"]/text()')
            # print(fenlei)
            # print(name)  # 建议debug而不是print，不然因为并发会重复打印

            item = MovieItem()
            item['name'] = name   # item['name'] = name
            # item.data = fenlei
            yield item  # 相当于同步脚本方法中的return

        # pass
