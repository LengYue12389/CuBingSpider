# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import MySQLdb


class CubingspiderPipeline:
    # 将数据保存到数据库
    def __init__(self):
        self.db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="panshidi", db="cubing", port=3306, charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        try:
            insert_sql = '''
                INSERT INTO cubing_table(name, wca_id, region, sex, experience, frequency, url_id) VALUES(%s, %s, %s, %s, %s, %s, %s)
            '''
            self.cursor.execute(insert_sql, (item['name'], item['wca_id'], item['region'], item['sex'],
                                             item['experience'], item['frequency'], item['url_id']))
            self.db.commit()
            return item
        except Exception as e:
            print(e)

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.db.close()
