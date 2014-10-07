# -*- coding: utf-8 -*-

# Scrapy settings for housing_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'housing_scraper'

SPIDER_MODULES = ['housing_scraper.spiders']
NEWSPIDER_MODULE = 'housing_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'housing_scraper (+http://www.yourdomain.com)'
