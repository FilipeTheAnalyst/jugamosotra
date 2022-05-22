import scrapy
from ..items import JugamosotraItem
from datetime import date


class JugamosSpider(scrapy.Spider):
    name = 'jugamos'
    start_urls = ['https://jugamosotra.com/es/24-juegos']

    def parse(self, response):
        for games in response.css("h2.h3.product-title"):
            yield response.follow(games.css('a ::attr(href)').get(), callback=self.parse_games)

            next_page = response.css(
                "a.next.js-search-link ::attr(href)").get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

    def parse_games(self, response):
        items = JugamosotraItem()
        try:
            items['id'] = int(response.css(
                "datos-juego-bgg ::attr(id-juego)").get())
        except:
            items['id'] = int(response.css(
                "div.product-description a::attr(href)").re("\d+")[0])
        items['name'] = response.css("h1.h1 ::text").get().strip()
        items['price'] = float(response.css('span[itemprop="price"] ::text').get(
        ).replace("\xa0", "").replace("€", "").replace(",", "."))
        items['availability'] = response.css(
            'span[id="product-availability"] ::text').getall()[-1].replace("\n", "")
        items['url'] = response.css('link[rel="canonical"] ::attr(href)').get()
        try:
            items['bgg_url'] = response.css(
                "div.product-description a::attr(href)").get()
        except:
            print("Nao existe")
        items['date'] = date.today()
        yield items
