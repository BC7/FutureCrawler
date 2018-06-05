import scrapy 

class ArticleSpider(scrapy.Spider):
    name = "articles"
    start_urls = ["https://futurism.com/tag/feature/"]

    # def start_requests(self):  
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'futurism-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

