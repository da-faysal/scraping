# Import required modules
import scrapy
import pandas as pd
from courseInfo.items import CourseinfoItem
import numpy as np


class CourseInfoScraper(scrapy.Spider):
	name="infoScraper"

	# Read in course link file
	today = pd.to_datetime("today").strftime("%d_%b_%y")
	linkDf = pd.read_csv(f"/home/faysal/Desktop/reed-scrapy/anyProvider/courseLink/{today}_courseLink.csv")

	# Make absolute links. This part keeps the unique course links only
	linkDf.courseLink = "https://www.reed.co.uk" + linkDf.courseLink
	linkDf = linkDf.squeeze() # Dataframe into series
	splitTempSeries = linkDf.astype("str").str.split("/", expand=True)
	splitTempSeries.columns = ["a","b","c","d","e","f","g","h", "i"]
	duplicatesDropped = splitTempSeries.drop_duplicates("f", keep="first").reset_index(drop=True)
	courseLink = duplicatesDropped.apply(lambda x: "/".join(x.values.astype("str")), axis=1) # This returns a series of course links
	start_urls = courseLink.tolist() # Scrape by chunks to run 2 spiders parallely


	def parse(self, response):
		item = CourseinfoItem()

		# Insert date
		item["date"] = pd.to_datetime("today").strftime("%d_%b_%y")

		# Scrape course title
		item["courseTitle"] = response.css("div.course-title h1::text").get(default="na").strip()

		# Scrape subtitle
		item["subtitle"] = response.css("div.course-title h2::text").get(default="na").strip()

		# Scrape course provider
		try:
			try:
				# If the provider is hyperlinked
				item["courseProvider"] = response.css("a.provider-link::text").get().strip()
			except:
				# If the provider is not hyperlinked
				item["courseProvider"] = response.css("span.thumbnail::text").get().strip()
		except:
			item["courseProvider"] = "na"

		# Scrape offer price
		try:
			offerPrice = response.css("span.current-price::text").get().replace(",", "").replace("£", "").replace("Free", "0")
			item["offerPrice"] = pd.to_numeric(offerPrice, errors="coerce")
		except:
			item["offerPrice"] = np.nan

		# Scrape original price
		try:
			originalPrice = response.css("small.vat-status::text").re(r"£\d*,?\d*")[0].replace(",", "").replace("£", "")
			item["originalPrice"] = pd.to_numeric(originalPrice, errors="coerce")
		except:
			item["originalPrice"] = np.nan

		# Scrape unit sold
		unitSold = response.css("#number-enquiries-purchases strong::text").get(default="0").strip()
		# Convert string inti "nan"
		unitSold = pd.to_numeric(unitSold.replace(",", ""), errors="coerce")
		# Replace "nan" by 0
		item["unitSold"] = unitSold if unitSold else 0


		# Check if the course was sold or enquired
		item["soldOrEnq"] = 2 if (response.css("#addToBasket") and response.css("#enquireNow"))\
		                    else 1 if response.css("#addToBasket")\
		                    else 0

		# Scrape savings
		savingsPercent = response.css(".icon-savings-tag.price-saving::text").get(default="0").replace("Save", "").replace("%", "").strip()
		item["savingsPercent"] = int(savingsPercent)

		# Extract course link
		item["courseLink"] = response.url

		# Does the course have CPD?
		item["haveCpd"] = 1 if response.css("div.badge.badge-dark.badge-cpd.mt-2").get()\
						  else 0


		# CPD point of the course
		# Extract text starts with min 1 and max 3 digits, followed by "CPD hours / points"
		cpdPoint = response.xpath("string(//body)").re(r"\d{1,3} CPD hours / points")
		cpdPoint = cpdPoint[0].strip().split("CPD")[0].strip() if item["haveCpd"] else 0
		item["cpdPoint"] = int(cpdPoint)

		# Awarding body of the course if any
		try:
			try:
				# Executes if the course is "Endorsed by"
				item["awardingBody"] = response.css("div.col a::text").get().strip()
			except:
				# Executes if the course is "Awarded by"
				item["awardingBody"] = response.css("div.small div a::text").get().strip()
		except:
			item["awardingBody"] = "na"

		# Qualification name of the course if any, only for awarded courses
		item["qualName"] = response.css("div.small h3.h4::text").get(default="na").strip()


		# Is the course regulated?
		item["isRegulated"] = 1 if response.css("div.badge.badge-dark.badge-regulated.mt-2").get()\
							else 0


		# Does the course have professional certification?
		item["hasProfCert"] = 1 if response.css("div.badge.badge-dark.badge-professional.mt-2").get()\
							else 0


		# Scrape category, broad categories and sub categories
		category = [x.strip() for x in response.css("ol.breadcrumb.pb-0 li.breadcrumb-item ::text").getall()]
		category = list(filter(lambda x: x, category))

		# Course category of the course
		item["category"] = category

		# Extract broad category 1
		try:
		    item["broadCategory1"] = category[0]
		except:
		    item["broadCategory1"] = "na"

		# Extract sub category 1
		try:
		    item["subCategory1"] = category[1]
		except:
		    item["subCategory1"] = "na"

		# Extract broad category 2    
		try:
		    item["broadCategory2"] = category[-2]
		except:
		    item["broadCategory2"] = "na"

		# Extract sub category 2
		try:
		    item["subCategory2"] = category[-1]
		except:
		    item["subCategory2"] = "na"

		# Extract course id from course link
		item["courseId"] = int(item["courseLink"].split("/")[5].replace("#",""))

		yield item



