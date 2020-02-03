# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokedexItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    national = scrapy.Field()
    name = scrapy.Field()
    types = scrapy.Field()
    species = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    main_ability = scrapy.Field()
    hidden_ability = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    sp_attack = scrapy.Field()
    sp_defense = scrapy.Field()
    speed = scrapy.Field()
    total_stats = scrapy.Field()
