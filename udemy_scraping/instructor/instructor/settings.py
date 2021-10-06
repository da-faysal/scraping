# import pandas as pd
# today = pd.to_datetime("today").strftime("%d_%b_%y")

BOT_NAME = 'instructor'

SPIDER_MODULES = ['instructor.spiders']
NEWSPIDER_MODULE = 'instructor.spiders'

# FEED_FORMAT = "csv"
# FEED_URI = f"{today}_instructorInfo.csv"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# Set user agent to avoid "403" error
USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

# Obey robots.txt rules
# Make robot.txt False
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False