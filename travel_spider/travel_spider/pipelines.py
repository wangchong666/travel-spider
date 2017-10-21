# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class TravelSpiderPipeline(object):
    
    def __init__(self):
        """Opens a mongo connection pool"""
        client = MongoClient('mongodb://mongo:27017/')
        self.posts = client.travel.posts;



    def process_item(self, item, spider):
<<<<<<< HEAD
        print(item["name"])
        post = {"name": item["name"],
         "site": item["site"],
         "address":item["address"],
         "category": item["category"],
         "en":{
             "title":item["title"],
             "location":item["location"],
             "date":item["date"],
             "content":item["content"],
         }}
        self.posts.insert_one(post)
=======
>>>>>>> 755bcf2f066b64f4c17eb26e4e42b80a21aa12ff
        return item
