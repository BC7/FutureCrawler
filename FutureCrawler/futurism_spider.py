import scrapy 
import json
from csvmanager import CsvManager
import os

class ArticleSpider(scrapy.Spider):
    name = "articles"
    start_urls = ["https://futurism.com/tag/feature/"]
    posts = []

    # def start_requests(self):  
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'futurism-parsed.json' #'futurism-%s.html' % page
        postshtml = response.css("div.post")

        for index in range(len(postshtml)):
            postdata = {
                'title': postshtml[index].xpath('//a[@class="title"]/@title').extract()[index].replace(',','-'),
                'url': postshtml[index].xpath('//a[@class="title"]/@href').extract()[index],
                'published': postshtml[index].xpath('//span[@class="time"]/text()').extract()[index].replace(',',' '),
                'tags': str(postshtml[index].css('div.tags a::text').extract()).replace(', ', '  ')#xpath('/div[@class="tags"]/a/text()').extract()).replace(', ',' ')
            }
            self.posts.append(postdata)
        
        csv = CsvManager(page + ".csv")
        csv.getKeys(self.posts[0])
        csv.updateCSV(self.posts)
       
        print('\n\n\n' + response.url + ' crawled successfully.. \nStored in: ' + os.getcwd() +'/'+ csv.file)

