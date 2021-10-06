
import scrapy

# Items to be scraped
class CourseItem(scrapy.Item):
	courseTitle = scrapy.Field()
	subtitle = scrapy.Field()
	courseLink = scrapy.Field()
	unitSold = scrapy.Field()
	courseRating = scrapy.Field()
	lastUpdated = scrapy.Field()
	courseLanguage = scrapy.Field()
	broadCategory = scrapy.Field()
	subcategory = scrapy.Field()
	subcategory1 = scrapy.Field()
	instructorRating = scrapy.Field()
	instructorTotalCourse = scrapy.Field()
	instructorLink = scrapy.Field()
	# offerPrice = scrapy.Field()
	# originalPrice = scrapy.Field()
	# courseDuration = scrapy.Field()
