# This Python file uses the following encoding: utf-8
import scrapy
import re
from scrapy.link import Link
from scrapy.spiders import CrawlSpider, Rule
from travel_spider.items import TravelSpiderItem
from scrapy.utils.project import get_project_settings
import json
from pymongo import MongoClient




class MeravigliapaperSpider(CrawlSpider):
    name = "meravigliapaper"
    allowed_domains = ["meravigliapaper.com"]
    start_urls = ["http://meravigliapaper.com/en/"]

    def start_requests(self):
        # settings = get_project_settings()
        return [scrapy.FormRequest(url="http://meravigliapaper.com/en/",callback=self.parse_total)]

    def load_pids(self):
        if not hasattr(self,'pids'):
            client = MongoClient('mongodb://mongo:27017/')
            all = client.travel.posts.find({}, {"address":1,"_id":0});
            self.urls = set()
            for data in all:
                self.urls.add(data["address"])
             
    def parse_details(self, response):
        self.load_pids()
        urls = response.xpath("//div[@id='wpex-grid-wrap']/article/a/@href").extract()
        print(urls)
        for url in urls:
            if url not in self.urls:
                self.urls.add(url)
                yield scrapy.Request(url=url,callback=self.parse_item)

    def parse_total(self, response):
        pop = response.xpath("//div[@class='page-of-page']/span/text()").extract()[0]
        f = 'http://meravigliapaper.com/en/page/{0}/'
        pages = int(pop.split(" ")[2]);
        urls = [scrapy.FormRequest(url=f.format(i),callback=self.parse_details) for i in range(1,pages+1)]
        print(urls)
        return urls;
        pass
    # def parse(self, response):
    #     print(response.url);
    def parse_item(self, response):
        #self.log('Hi, thisi is an item page! %s' % response.url)

        # if response.status in [301, 302] and 'Location' in response.headers:
        #     # test to see if it is an absolute or relative URL
        #     #print(response.status)
        #     newurl = response.headers['location'].decode('utf-8')
        #     if "sec.alibaba.com" in newurl or "login" in newurl:
        #           return  scrapy.FormRequest(url = response.url, meta = response.meta, callback=self.parse_item)     
        #     return  scrapy.FormRequest(url = newurl, meta = response.meta, callback=self.parse_item) 
        
        item = TravelSpiderItem()
        item['title']="";
        item['location']="";
        content = response.xpath('//div[@id="post"]/div/article').extract()[0];
        try:

            item['date'] = response.xpath('//div[@id="post"]/div/header/section/div/text()').extract()[0];
            item['category'] = response.xpath('//div[@id="post"]/div/header/section/ul/li/a/text()').extract()[0];
            item['address'] = response.url
            item['name'] = re.search(r'meravigliapaper.com(/en)?/.+?/(.*?)/',response.url).group(2)
            item['content'] = content
            item['site'] = "meravigliapaper"
            item['title'] = response.xpath('//div[@id="post"]/div/header/h1/text()').extract()[0];
            item['location'] = response.xpath('//div[@id="post"]/div/header/h2/text()').extract()[0];

        except Exception as e:
            self.logger.error(response.url)
            #raise e
        return item

