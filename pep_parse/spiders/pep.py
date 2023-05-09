import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.css('a[href^="pep-"]')
        for pep_link in all_pep:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text').get()
        pep_info_items = title.replace('PEP', ' ').split('–')
        pep_parse_data = {
            'number': pep_info_items[0].replace(' ', ''),
            'name': pep_info_items[1][1:],
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(pep_parse_data)
