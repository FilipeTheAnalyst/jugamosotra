import scrapy
from ..items import JugamosotraItem
from datetime import date
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re


class JugamosSpider(scrapy.Spider):
    name = 'jugamos'
    start_urls = ['https://jugamosotra.com/es/24-juegos']

    def parse(self, response):
        for games in response.css("h2.h3.product-title"):
            url = games.css('a ::attr(href)').get()
            yield SeleniumRequest(
                url=url,
                wait_time=3,
                callback=self.parse_games,
                wait_until=EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'valoracion'))
            )
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

        items['min_players'] = int(response.css("div.destacado ::text")[
            3].get().strip().split(' - ')[0])
        items['max_players'] = int(response.css("div.destacado ::text")[
            3].get().strip().split(' - ')[1])
        items['best_player_count'] = int(response.css("div.destacado ::text")[
            5].get().strip())
        items['duration_min'] = response.css("div.destacado ::text")[
            7].get().replace('min', '').strip()
        items['min_age'] = int(response.css("div.destacado ::text")[
            9].get().strip().replace('+', ''))
        items['weight'] = response.css("div.destacado ::text")[
            11].get().split('/')[0].strip()
        yield items
