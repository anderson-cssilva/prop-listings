import scrapy

class QuotesSpider(scrapy.Spider):
    name = "vidal"

    def start_requests(self):
        urls = [
            'https://vidalimoveis.imb.br/comprar/valor-max_3000000/ordem-valor/resultado-crescente/quantidade-48/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for prop in response.css("div.todos_imoveis a"):
            yield {
                'link' : prop.attrib['href'],
                'prop_id' : prop.css("div.resultado").attrib['id'],
                'neighbourhood' : prop.css("div.resultado").css("div.dados").css("h4.localizacao span::text").get(),
                'price' : prop.css("div.resultado").css("div.dados").css("div.alinha_valores h5::text").get(),
            }

        next_page = response.css("a.page-link").attrib['href']
        next_page = next_page[next_page.find('(')-1:next_page.find(')')]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
