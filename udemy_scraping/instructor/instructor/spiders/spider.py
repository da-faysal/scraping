# Import required modules
import pandas as pd
import re
import scrapy
from instructor.items import InstructorItem

# Spider class
class InstructorScraper(scrapy.Spider):
	name="instructorInfo"
	courseDf = pd.read_csv("/home/faysal/Desktop/udemy_scrapy/course/officeProductivity_courseInfo.csv")
	courseDf = courseDf[courseDf.instructorLink!="na"] # Drop invalid links
	start_urls = courseDf.instructorLink.to_list()



	def parse(self, response):
		item = InstructorItem()
		
		# Get request  link
		item["instructorLink"] = response.url
		
		# Scrape instructor link
		item["instructorName"] = response.css("h1.udlite-heading-serif-xxxl::text").get(default="na").strip()
		
		# SCrape instructor name
		item["instructorProf"] = response.css("h2.udlite-heading-md.instructor-profile--instructor-title--2VTBB::text").get(default="na").strip()

		# Scrape instructor total student
		try:
			instructorTotalStudent = response.css("div.udlite-heading-xl::text")[0].get().strip()
			instructorTotalStudent = "".join(re.findall(r"\d*,?", instructorTotalStudent)).replace(",", "")
			instructorTotalStudent = int(pd.to_numeric(instructorTotalStudent, errors="coerce"))
			item["instructorTotalStudent"] = instructorTotalStudent
		except:
			item["instructorTotalStudent"] = 0

		# Scrape instructor total review
		try:
			instructorTotalReview = response.css("div.udlite-heading-xl::text")[1].get().strip()
			instructorTotalReview = "".join(re.findall(r"\d*,?", instructorTotalReview)).replace(",", "")
			instructorTotalReview = int(pd.to_numeric(instructorTotalReview, errors="coerce"))
			item["instructorTotalReview"] = instructorTotalReview
		except:
			item["instructorTotalReview"] = 0


		# Scrape instructor contacts
		try:
			instructorContact = response.css("div.instructor-profile--social-links--3Kub5 a::attr(href)").getall()
			item["instructorContact"] = instructorContact if instructorContact else "na"
		except:
			item["instructorContact"] = "na"
		
		yield item
