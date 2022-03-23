import scrapy
from CuBingSpider.items import CubingspiderItem


class CubingSpider(scrapy.Spider):
    name = 'cubing'
    allowed_domains = ['cubing.com']
    start_urls = ['https://cubing.com/results/person?region=World']

    def parse(self, response):
        # 创建一个CuBingSpider对对象
        cubing_items = CubingspiderItem()
       # 拿到详情页面的数据
        url_id = response.xpath('//tbody/tr[@class="odd" or @class="even"]/td[2]/a/@href').extract()
        for item in url_id:
            url_id = 'https://cubing.com/results/person/' + item[-10:]
            # print(url_id)
            yield scrapy.Request(url=url_id, callback=self.parse_details, meta={'cubing_items': cubing_items, 'url_id': url_id})
        # 拿到下一页的数据
        next_link = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # print(next_link[-4:])
        if next_link[-4:] != '1552':
            # print('https://cubing.com'+ next_link)
            yield scrapy.Request(url='https://cubing.com' + next_link, callback=self.parse)

    def parse_details(self, response):
        cubing_items = response.meta.get('cubing_items', '')
        url_id = response.meta.get('url_id', '')
        # 解析各个字段的数据
        cubing_items['name'] = response.xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/span[2]/text()').extract()
        cubing_items['experience'] = response.xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div[3]/span[2]/text()').extract()
        cubing_items['frequency'] = response.xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div[6]/span[2]/text()').extract()
        cubing_items['sex'] = response.xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div[5]/span[2]/text()').extract()
        cubing_items['wca_id'] = response.xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div[4]/span[2]/text()').extract()
        cubing_items['region'] = response.xpath('/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div[2]/span[2]/text()').extract()
        cubing_items['url_id'] = url_id
        # print(cubing_items)
        yield cubing_items
    #     # print(cubing_items)
