# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JugamosotraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    availability = scrapy.Field()
    url = scrapy.Field()
    bgg_url = scrapy.Field()
    date = scrapy.Field()
    min_players = scrapy.Field()
    max_players = scrapy.Field()
    best_player_count = scrapy.Field()
    duration_min = scrapy.Field()
    min_age = scrapy.Field()
    weight = scrapy.Field()
