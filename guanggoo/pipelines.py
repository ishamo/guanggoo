# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import torndb
db = torndb.Connection('127.0.0.1', 'qdebug', 'root', '123456')

class GuanggooPipeline(object):
    def process_item(self, item, spider):
        return item


class SavePipeline(object):
    def process_item(self, item, spider):
        print(1111111111111, item, type(item))
        try:
            if item['title'] and item['url'] and item['content']:
                print(333333333333333333333333333333333333333333333333)
                db.query('insert into post(url, title, content) value (%s, %s, %s)',
                         item['url'], item['title'], item['content'])
                print('22222222222222222222222222, save an entity SUCCESSFULLY')
        except Exception:
            raise scrapy.exceptions.DropItem(item)
