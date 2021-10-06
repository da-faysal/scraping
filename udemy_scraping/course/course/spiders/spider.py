# Import required modules
import scrapy
from course.items import CourseItem
import pandas as pd
import re

class UdemyCourseScraper(scrapy.Spider):
	name="courseInfo"

	# Read in the course links
	linkDf = pd.read_excel("officeProductivity_courseLink.xlsx")
	start_urls = linkDf.courseLink.tolist()


	def parse(self, response):
		item = CourseItem()

		# SCrape course title
		item["courseTitle"] = response.css("[data-purpose='lead-title']::text").get(default="na").strip()

		# Scrape subtitle
		item["subtitle"] = response.css("[data-purpose='lead-headline']::text").get(default="na").strip()

		# Extract course link
		item["courseLink"] = response.url

		# Scrape unit sale
		try:
			unitSold = response.css("[data-purpose='enrollment']::text").get().strip()
			unitSold = "".join(re.findall(r"\d*,?", unitSold)).replace(",", "").strip()
			unitSold = int(pd.to_numeric(unitSold, errors="coerce"))
			item["unitSold"] = unitSold
		except:
			item["unitSold"] = 0
		

		# # Srrape offer price
		# item["offerPrice"] = response.css("[data-purpose='course-price-text'] span::text")[-1].get(default="na").strip()

		# # Scrape original price
		# item["originalPrice"] = response.css("[data-purpose='course-old-price-text']::text").get(default="na").strip()

		# # Scrape course duration
		# item["courseDuration"] = response.css("[data-purpose='video-content-length']::text").get(default="na").strip()
	
		# Scrape course rating
		try:
			courseRating = response.css("[data-purpose='rating-number']::text").get(default="0").strip()
			courseRating = "".join(re.findall(r"\d*\.?", courseRating)).strip()
			courseRating = pd.to_numeric(courseRating, errors="coerce")
			item["courseRating"] = courseRating
		except:
			item["courseRating"] = 0

		# Scrape last updated date
		try:
			lastUpdated = response.css("[data-purpose='last-update-date'] span::text")[-1].get().strip()
			item["lastUpdated"] = "".join(re.findall(r"\d*/\d*", lastUpdated))
		except:
			item["lastUpdated"] = "na"

		# SCrape course language
		try:
			item["courseLanguage"] = response.css("[data-purpose='lead-course-locale']::text")[-1].get().strip()
		except:
			item["courseLanguage"] = "na"

		# Scrape broad caregory
		try:
			item["broadCategory"] = response.css("div.topic-menu.udlite-breadcrumb a.udlite-heading-sm::text")[0].get().strip()
		except:
			item["broadCategory"] = "na"

		# Scrape subcategory
		try:
			item["subcategory"] = response.css("div.topic-menu.udlite-breadcrumb a.udlite-heading-sm::text")[1].get().strip()
		except:
			item["subcategory"] = "na"

		# Scrape subcategory 1
		try:
			item["subcategory1"] = response.css("div.topic-menu.udlite-breadcrumb a.udlite-heading-sm::text")[-1].get().strip()
		except:
			item["subcategory1"] = "na"


		# Scrape instructor rating
		try:
			instructorRating = "".join(response.css(".udlite-block-list-item-content::text").re(r"\d*\.?\d*\s?Instructor Ratings?")[-1])
			instructorRating = "".join(re.findall(r"\d*\.?", instructorRating)).strip()
			instructorRating = pd.to_numeric(instructorRating, errors="coerce")
			item["instructorRating"] = instructorRating
		except:
			item["instructorRating"] = 0

		# Scrape instructor total courses
		try:
			instructorTotalCourse =  "".join(response.css(".udlite-block-list-item-content::text").re(r"\d*,?\d*\s?Courses?")[-1])
			instructorTotalCourse = "".join(re.findall(r"\d*,?", instructorTotalCourse)).replace(",", "").strip()
			instructorTotalCourse = int(pd.to_numeric(instructorTotalCourse, errors="coerce"))
			item["instructorTotalCourse"] = instructorTotalCourse
		except:
			item["instructorTotalCourse"] = 1

		# Scrape instructor link
		try:
			item["instructorLink"] = "https://www.udemy.com" + response.css(".udlite-heading-lg.instructor--instructor__title--34ItB a").attrib["href"]
		except:
			try: 
				item["instructorLink"] = "https://www.udemy.com" + response.css(".instructor-links--names--7UPZj a").attrib["href"]
			except:
				item["instructorLink"] = "na"
			
		return item
