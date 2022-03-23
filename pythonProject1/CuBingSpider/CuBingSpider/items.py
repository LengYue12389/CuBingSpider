# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CubingspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 拿到选手的基本信息
    name = scrapy.Field()
    wca_id = scrapy.Field()
    region = scrapy.Field()
    sex = scrapy.Field()
    # 拿到详情页面的数据
    # 参赛经历
    experience = scrapy.Field()
    # 参赛次数
    frequency = scrapy.Field()
    url_id = scrapy.Field()





