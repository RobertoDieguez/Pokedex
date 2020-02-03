import scrapy
from ..items import PokedexItem

class PokedexSpider(scrapy.Spider):
    name = "pokedex"
    start_urls = ["https://pokemondb.net/pokedex/bulbasaur"] #We start with bulbasaur and go to the next pokemon
    item = PokedexItem()
    counter = 1
    
    pokedex_data = {
        'types': 'tr:nth-child(2) a.type-icon::text',
        'species': 'tr:nth-child(3) td::text',
        'height': 'tr:nth-child(4) td::text',
        'weight': 'tr:nth-child(5) td::text',
        'main_ability': 'tr:nth-child(6) span a::text',
        'hidden_ability': 'tr:nth-child(6) small a::text'  
    }

    base_stats = {
        'hp' : 'tr:nth-child(1) td:nth-child(2)::text',
        'attack' : 'tr:nth-child(2) td:nth-child(2)::text',
        'defense' : 'tr:nth-child(3) td:nth-child(2)::text',
        'sp_attack' : 'tr:nth-child(4) td:nth-child(2)::text',
        'sp_defense' : 'tr:nth-child(5) td:nth-child(2)::text',
        'speed' : 'tr:nth-child(6) td:nth-child(2)::text',
        'total_stats': 'tfoot tr b::text'
        
    }

    def parse(self, response):
        pokedex_table = response.css('.text-center+ .span-lg-4 table.vitals-table tbody')
        stats_table = response.css('#tab-basic-' + str(self.counter) + ' .span-lg-8 table.vitals-table')
        self.item['national'] = self.counter
        self.item['name'] = response.css('h1::text').get()
        for key, value in self.pokedex_data.items():
            self.item[key] = pokedex_table.css(value).extract()

        for key, value in self.base_stats.items():
            self.item[key] = stats_table.css(value).extract()

        yield self.item

        next_pokemon = response.css('a.entity-nav-next::attr(href)').get()
        print(next_pokemon)
        if next_pokemon is not None:
            self.counter += 1
            yield response.follow('https://pokemondb.net/' + next_pokemon, callback = self.parse)