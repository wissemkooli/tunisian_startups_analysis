# tunisian_startups/items.py
import scrapy

class TunisianStartupsItem(scrapy.Item):
    # The name of the startup
    name = scrapy.Field()
    
    # The industry or sector the startup operates in (e.g., FinTech, E-commerce)
    sector = scrapy.Field()
    
    # The year the startup was founded
    year_founded = scrapy.Field()
    
    # The date the startup received its label/status (meaning depends on the source)
    label_date = scrapy.Field()
    
    # The URL of the startup's official website
    website = scrapy.Field()
    description = scrapy.Field()
    founders = scrapy.Field()
    email = scrapy.Field()


    