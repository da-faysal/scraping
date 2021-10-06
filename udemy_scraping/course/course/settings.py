
# import pandas as pd
# today = pd.to_datetime("today").strftime("%d_%b_%y")

BOT_NAME = 'course'

SPIDER_MODULES = ['course.spiders']
NEWSPIDER_MODULE = 'course.spiders'

# FEED_FORMAT = "csv"
# FEED_URI = f"{today}_courseInfo.csv"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# Set user agent to avoid "403" error
USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32


# Disable cookies (enabled by default)
#COOKIES_ENABLED = False