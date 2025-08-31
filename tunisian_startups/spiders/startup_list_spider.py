# tunisian_startups_clean/spiders/startup_api_spider.py
import scrapy
import json
from ..items import TunisianStartupsItem

class StartupApiSpider(scrapy.Spider):
    name = "startup_api"
    
    def start_requests(self):
        # The exact API endpoint you found
        api_url = "https://startups.smartcapital.tn/7lan"
        yield scrapy.Request(api_url, callback=self.parse_api)

    def parse_api(self, response):
        """
        Parse the JSON API response
        """
        try:
            data = json.loads(response.text)
            print(f" Successfully loaded {len(data)} startups from API")
            
        except json.JSONDecodeError as e:
            print(f" Failed to parse JSON: {e}")
            return

        # Process each startup in the JSON data
        for startup_data in data:
            item = TunisianStartupsItem()
            
            # Map the JSON fields to your item fields (based on the structure you found)
            item['name'] = startup_data.get('name')
            item['sector'] = startup_data.get('sector') or startup_data.get('industry')
            item['year_founded'] = startup_data.get('creation_year')
            item['label_date'] = startup_data.get('label')
            item['website'] = startup_data.get('website')
            # You can add more fields if you want
            item['description'] = startup_data.get('desc')
            item['founders'] = ', '.join(startup_data.get('founders', [])) if startup_data.get('founders') else None
            item['email'] = startup_data.get('email')
            
            yield item




