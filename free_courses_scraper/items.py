# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    """Define the fields for course data"""

    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
