import pandas as pd
today = pd.to_datetime("today").strftime("%d_%b_%y")

BOT_NAME = 'courseLink'

SPIDER_MODULES = ['courseLink.spiders']
NEWSPIDER_MODULE = 'courseLink.spiders'


FEED_FORMAT = "csv" 
FEED_URI = f"{today}_courseLink.csv"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True