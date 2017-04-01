# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors

# Connect to the database




class XinwenPipeline(object):
    def open_spider(self,spider):
        self.f=open('xinwen.txt','w')

    def close_spider(self,spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line=str(dict(item))+'\n'
            self.f.write(line)
        except:
            pass


        connection = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='toor',db='xinwen',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql = 'INSERT INTO xinwen (url, title, content) VALUES (\'%s\', \'%s\', \'%s\')'
            a=dict(item)
            cursor.execute(sql%(a['url'],a['title'],a['content']))
        connection.commit()
        connection.close()
        return item
