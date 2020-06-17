import scrapy
from bs4 import BeautifulSoup
from bgmedic.items import DiseaseItem

class DiseasesSpider(scrapy.Spider):
    base_url = 'https://www.bgmedic.com'
    name = 'diseases'
    start_urls = ['https://www.bgmedic.com/systoyaniya-i-zabolyavaniya']

    def parse(self, response):
        categories = response.css('div.category_list > ul > li')
        for category in categories:
            url = self.base_url + category.css('a::attr(href)').get()
            yield response.follow(url, self.parse_disease_category)

    def parse_disease_category(self, response):
        diseases = response.css('div.listofarticles.col2txt > ul > li')
        for disease in diseases:
            url = self.base_url + disease.css('a::attr(href)').get()
            yield response.follow(url, self.parse_disease_information)

    def parse_disease_information(self, response):
        disease = DiseaseItem()
        disease['title'] = response.css('article.itemView > header > h1::text').get()

        disease_text = BeautifulSoup(response.css('div.myitemtemplate').extract()[0], 'lxml').text
        disease['text'] = disease_text.replace('\xa0', '').replace('\n', ' ').replace('"', '').strip('\n').strip()

        yield disease
