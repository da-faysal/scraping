#Import modules
import scrapy

# Define items here
class TrustpilotScrapingItem(scrapy.Item):
    reviewer = scrapy.Field()
    review_body = scrapy.Field()
    rating = scrapy.Field()
    location = scrapy.Field()
    review_header = scrapy.Field()
    review_date = scrapy.Field()
