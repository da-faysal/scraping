# Import required modules
import re
from bs4 import BeautifulSoup
import requests
import scrapy
import numpy as np
from itertools import chain

# These are the prodivers we would like to scrape
providerCoverPage = ['https://www.reed.co.uk/courses/one-education/p1812',
 'https://www.reed.co.uk/courses/janets/p1778',
 'https://www.reed.co.uk/courses/training-express-ltd/p2079',
 'https://www.reed.co.uk/courses/academy-for-health-fitness/p2261',
 'https://www.reed.co.uk/courses/be-acouk/p545',
 'https://www.reed.co.uk/courses/cpd-courses/p1534',
 'https://www.reed.co.uk/courses/brentwood-open-learning-college/p438',
 'https://www.reed.co.uk/courses/oplex-careers/p630',
 'https://www.reed.co.uk/courses/oxford-home-study-college/p1245',
 'https://www.reed.co.uk/courses/the-training-terminal/p1064',
 'https://www.reed.co.uk/courses/excel-with-business/p930',
 'https://www.reed.co.uk/courses/ofcourse/p675',
 'https://www.reed.co.uk/courses/trendimi/p964',
 'https://www.reed.co.uk/courses/centre-of-excellence-online/p652',
 'https://www.reed.co.uk/courses/lead-academy/p2144',
 'https://www.reed.co.uk/courses/beke-college-cic/p2140',
 'https://www.reed.co.uk/courses/protrainings-europe-limited/p981',
 'https://www.reed.co.uk/courses/mandatory-compliance/p1514',
 'https://www.reed.co.uk/courses/international-open-academy/p967',
 'https://www.reed.co.uk/courses/skill-up/p2339',
 'https://www.reed.co.uk/courses/simply-cert/p669',
 'https://www.reed.co.uk/courses/course-cloud/p2413',
 'https://www.reed.co.uk/courses/the-teachers-training/p2334',
 'https://www.reed.co.uk/courses/1-training/p1312',
 'https://www.reed.co.uk/courses/institute-of-beauty-and-makeup/p2509',
 'https://www.reed.co.uk/courses/the-animal-care/p2520',
 'https://www.reed.co.uk/courses/skill-express/p2510',
 'https://www.reed.co.uk/courses/compliance-central/p2584',
 'https://www.reed.co.uk/courses/skills-success/p1341',
 'https://www.reed.co.uk/courses/globaledulink/p533',
 'https://www.reed.co.uk/courses/uk-professional-development-academy-ltd/p1749',
 'https://www.reed.co.uk/courses/study365/p1060',
 'https://www.reed.co.uk/courses/staff-training-solutions/p1477',
 'https://www.reed.co.uk/courses/inspire-london-college-ltd/p1746',
 'https://www.reed.co.uk/courses/simpliv-llc/p1999',
 'https://www.reed.co.uk/courses/echo3-education-limited/p1619',
 'https://www.reed.co.uk/courses/life-saving-training-ltd/p2218',
 'https://www.reed.co.uk/courses/south-london-college/p1405',
 'https://www.reed.co.uk/courses/knowledge-door/p2538',
 'https://www.reed.co.uk/courses/holly-and-hugo/p965',
 'https://www.reed.co.uk/courses/course-pride/p1706',
 'https://www.reed.co.uk/courses/active-recruitment-ltd/p2041',
 'https://www.reed.co.uk/courses/e-careerslifestyle/p1733',
 'https://www.reed.co.uk/courses/eventtrix/p966',
 'https://www.reed.co.uk/courses/apex-learning/p2601',
 'https://www.reed.co.uk/courses/studyhub/p2675',
 'https://www.reed.co.uk/courses/next-level-academy/p1727',
 'https://www.reed.co.uk/courses/course-central/p2713',
 'https://www.reed.co.uk/courses/elearn-college/p1254',
 'https://www.reed.co.uk/courses/business-training-world/p1232']


# This function generates cover pages for each provider
def generateCoverPage(url):
	"""url = provider directory link,
	return = cover pages"""
	
	coverPage = []
	HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
	r = requests.get(url, headers=HEADERS)
	s = BeautifulSoup(r.text, "lxml")
	totalCourse = int(s.find("span", class_="h1").text.strip().replace(",", ""))
	totalPage = int(np.ceil(totalCourse/100))
	for pg in range(1, totalPage+1):
		coverPage.append(url + f"?pageno={pg}&sortby=MostPopular&pagesize=100")
	return coverPage


class CourseLinkScraper(scrapy.Spider):
	name="linkScraper"
	urls = list(map(generateCoverPage, providerCoverPage))
	urls = list(chain.from_iterable(urls))
	start_urls = urls*6


	def parse(self, response):
		mainContainer = response.css("div.mobile-clickable-area")
		for cont in mainContainer:
			yield {"courseLink":cont.css(".course-overview a::attr(href)").getall()}
