import scrapy
from bs4 import BeautifulSoup
from framar.items import DiseaseItem

class DiseasesSpider(scrapy.Spider):
    name = 'diseases'
    start_urls = ['https://medpedia.framar.bg/%D0%B7%D0%B0%D0%B1%D0%BE%D0%BB%D1%8F%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F']

    def parse(self, response):
        disease_categories = response.css('div.box.npt > ul.ui.list.tree > li.item')
        for disease_category in disease_categories:
            url = disease_category.css('div.content > h2.header.nb > a.blue::attr(href)').get()
            yield response.follow(url, self.parse_disease_category)

    def parse_disease_category(self, response):
        yield from self.parse_disease(response)

        disease_category_types = response.css('section.box > ul.ui.list.tree > li.item')
        for disease_category_type in disease_category_types:
            url = disease_category_type.css('div.content > span.header.nb > a.blue::attr(href)').get()
            yield response.follow(url, self.parse_disease_category_type)

    def parse_disease_category_type(self, response):
        yield from self.parse_disease(response)

        disease_subcategory_types = response.css('section.box > ul.ui.list.tree > li.item')
        for disease_subcategory_type in disease_subcategory_types:
            url = disease_subcategory_type.css('div.content > span.header.nb > a.blue::attr(href)').get()
            yield response.follow(url, self.parse_disease_subcategory_type)

    def parse_disease_subcategory_type(self, response):
        yield from self.parse_disease(response)

        disease_types = response.css('section.box > ul.ui.list.tree > li.item')
        for disease_type in disease_types:
            url = disease_type.css('div.content > span.header.nb > a.blue::attr(href)').get()
            yield response.follow(url, self.parse_disease_type)

    def parse_disease_type(self, response):
        yield from self.parse_disease(response)

    def parse_disease(self, response):
        disease = DiseaseItem()
        disease['title'] = response.css('h1.ui.header.h1::text').get()

        author = response.css('div.authorship.cl > span > a::text').get()
        if author is None:
            disease['author'] = 'Няма автор'
        else:
            disease['author'] = response.css('div.authorship.cl > span > a::text').get()

        disease['published'] = response.css('time.subheader::text').get()

        disease_text = BeautifulSoup(response.css('div.article > div.acc.box').extract()[0], 'lxml').text
        formatted_disease_text = disease_text.replace('\xa0', '').replace('\n', ' ').replace('"', '').strip('\n').strip()
        if formatted_disease_text is '':
            disease['text'] = 'Няма описание на заболяването.'
        else:
            disease['text'] = formatted_disease_text

        yield disease
