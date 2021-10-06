import scrapy

# Items to scrape
class InstructorItem(scrapy.Item):
	instructorName = scrapy.Field()
	instructorLink = scrapy.Field()
	instructorProf = scrapy.Field()
	instructorTotalStudent = scrapy.Field()
	instructorTotalReview = scrapy.Field()
	instructorContact = scrapy.Field()
