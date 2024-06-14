import scrapy

class JobItem(scrapy.Item):
    title = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    apply_url = scrapy.Field()
