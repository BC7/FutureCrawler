import scrapy 

class ArticleSpider(scrapy.Spider):
    name = "articles"

    def start_requests(self):
        start_urls = ["https://futurism.com/tag/feature/"]

    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

