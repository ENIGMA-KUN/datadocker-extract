import psycopg2

class JobsPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host='postgres',
            user='user',
            password='password',
            database='job_scraper'
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute(
            "INSERT INTO jobs (title, location, description, apply_url) VALUES (%s, %s, %s, %s)",
            (item['title'], item['location'], item['description'], item['apply_url'])
        )
        self.connection.commit()
        return item
