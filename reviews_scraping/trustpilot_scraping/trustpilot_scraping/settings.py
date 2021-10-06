# Scrapy settings for trustpilot_scraping project

BOT_NAME = 'trustpilot_scraping'

SPIDER_MODULES = ['trustpilot_scraping.spiders']
NEWSPIDER_MODULE = 'trustpilot_scraping.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'trustpilot_scraping (+http://www.yourdomain.com)'

# Obey robots.txt rules
# Make it False
ROBOTSTXT_OBEY = False
