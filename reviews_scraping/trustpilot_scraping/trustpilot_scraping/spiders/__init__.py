# Import required modules
import scrapy
import json
from trustpilot_scraping.items import TrustpilotScrapingItem

# Class for scraping
class ReviewScraper(scrapy.Spider):
    name="review_scraper"
    start_urls = [
        "https://www.trustpilot.com/review/janets.org.uk"
    ]


    def parse(self, response):
        item = TrustpilotScrapingItem()

        # Main container
        main_container = response.css("article.review")
        for cont in main_container:
            # Scrape reviewer
            item["reviewer"] = cont.css(".consumer-information__name::text").get(default="na").strip()

            # Scrape location
            item["location"] = cont.css(".consumer-information__location span::text").get(default="na").strip()

            # Get rating from image 'alt' attribute
            item["rating"] = cont.css(".star-rating.star-rating--medium img::attr(alt)").get().split(" ")[0]

            # Scrape review header
            item["review_header"] = cont.css(".link.link--large.link--dark::text").get(default="na").strip()

            # Scrape review body
            item["review_body"] = cont.css(".review-content__text::text").get(default="na").strip()

            # Scrape date
            date = cont.css("div.review-content-header__dates script::text").get()
            item["review_date"] = json.loads(date)["publishedDate"]
            yield item
        

        # Follow next page
        # Get next page link if exists
        next_page = response.css(".pagination-container.AjaxPager a::attr(href)").getall()[-1]
        
        # Go to next page if exists
        if next_page:
            abs_link = "https://www.trustpilot.com" + next_page
            yield scrapy.Request(url=abs_link)