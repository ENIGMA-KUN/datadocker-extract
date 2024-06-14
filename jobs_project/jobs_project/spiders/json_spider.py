import scrapy
import json
from jobs_project.items import JobItem

class JsonSpider(scrapy.Spider):
    name = 'json_spider'

    def start_requests(self):
        urls = [
            'file:///app/s01.json',
            'file:///app/s02.json'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        for job in data:
            item = JobItem()
            item['title'] = job['title']
            item['location'] = f"{job['city']}, {job['state']}"
            item['description'] = job['description']
            item['apply_url'] = job.get('apply_url', 'N/A')
            yield item
