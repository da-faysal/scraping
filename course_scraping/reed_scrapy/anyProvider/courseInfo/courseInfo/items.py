import scrapy

# Defines variables to scrape
class CourseinfoItem(scrapy.Item):
	date = scrapy.Field()
	courseId = scrapy.Field()
	courseTitle = scrapy.Field()
	subtitle = scrapy.Field()
	courseProvider = scrapy.Field()
	offerPrice = scrapy.Field()
	originalPrice = scrapy.Field()
	unitSold = scrapy.Field()
	soldOrEnq = scrapy.Field()
	courseLink = scrapy.Field()
	haveCpd = scrapy.Field()
	cpdPoint = scrapy.Field()
	awardingBody = scrapy.Field()
	qualName = scrapy.Field()
	isRegulated = scrapy.Field()
	savingsPercent = scrapy.Field()
	category = scrapy.Field()
	broadCategory1 = scrapy.Field()
	broadCategory2 = scrapy.Field()
	subCategory1 = scrapy.Field()
	subCategory2 = scrapy.Field()
	hasProfCert = scrapy.Field()