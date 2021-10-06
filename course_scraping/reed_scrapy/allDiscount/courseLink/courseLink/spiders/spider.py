# Import required modules
import scrapy
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


class CourseLinkSpider(scrapy.Spider):
	name="linkScraper"

	# Making request
	r = requests.get("https://www.reed.co.uk/courses/discount?pageno=1&sortby=MostPopular&pagesize=100")
	s = BeautifulSoup(r.text, "lxml")
	totalCourse = int(s.find("span", class_="h1").text.strip().replace(",", ""))
	totalPage = int(np.ceil(totalCourse/100))

	# To store start urls
	start_urls = []
	for pg in range(1, totalPage+1):
		start_urls.append(f"https://www.reed.co.uk/courses/discount?pageno={pg}&sortby=MostPopular&pagesize=100")
	start_urls = start_urls*6


	def parse(self, response):
		for cont in response.css("div.mobile-clickable-area"):
			yield {
			"courseLink": cont.css(".course-overview a::attr(href)").getall()
			}

