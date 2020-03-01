import scrapy

class QuotesSpider(scrapy.Spider):
    name = "lamerhaber"
    start_urls = [
    'https://lamerhaber.com/',
    'https://lamerhaber.com/category/hack-haber/',
    'https://lamerhaber.com/category/ozel-haberler/',
    'https://lamerhaber.com/category/hack-gruplari/',
    'https://lamerhaber.com/category/haberler/',
    'https://lamerhaber.com/category/teknoloji/',
    'https://lamerhaber.com/category/duyurular/'
    ]
    def parse(self, response):
        for icerik in response.css('header.post-header'):
            yield {
            'kategori': icerik.css('p.post-categories a::text').get(),
            'baslik': icerik.css('h2 a::text').get(),
            'tarih': icerik.css('p.post-meta a::text').get()
            }
