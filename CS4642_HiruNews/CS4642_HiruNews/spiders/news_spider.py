import scrapy


class NewsSpider(scrapy.Spider):

    name = "News"

    start_urls = [
        'http://www.hirunews.lk/all-news.php'
    ]

    def parse(self, response):
        for news in response.css('div.rp-mian'):
            yield {
                'time': news.css('div.time::text').extract_first(),
                'title': news.css('div.lts-cntp a::text').extract_first(),
                'text': news.xpath('div[@class="lts-txt2"]/text()').extract_first(),
                'link': news.xpath('div[@class="lts-txt2"]/a/@href').extract_first()
            }

        next_page = response.css('div.pagi_2').xpath('a[@title="next page"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
