import scrapy 

class ArticleSpider(scrapy.Spider):
    name = "articles"
    start_urls = ["https://futurism.com/tag/feature/"]
    posts = []

    # def start_requests(self):  
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'futurism-parsed.json' #'futurism-%s.html' % page
        posts = response.css("div.post")
        for index in range(len(posts)):
            postdata = {
                'title': posts[index].xpath('//a[@class="title"]/@title').extract()[index],
                'url': posts[index].xpath('//a[@class="title"]/@href').extract()[index],
                'published': posts[index].xpath('//span[@class="time"]/text()').extract()[index]
            }
            # print('\n\nDetails : \n' + posts[index].xpath('//a[@class="title"]/@title').extract()[index])
            self.posts.append(postdata)
        with open(filename, 'w+') as f:
            f.write(str(self.posts))
        print('\n\n\nArticle url : ' + self.posts[0]['url'])

