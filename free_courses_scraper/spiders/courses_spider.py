import scrapy
from free_courses_scraper.items import CourseItem
import re


class CoursesSpiderSpider(scrapy.Spider):
    name = "courses_spider"
    allowed_domains = ["answersq.com"]
    start_urls = ["https://answersq.com"]

    def parse(self, response):
        """Parse the main page and extract course information"""

        course_items = response.css("ul li")
        current_date = None

        for item in course_items:
            text = item.css("::text").get()
            if text and "Udemy Free Courses for" in text:
                current_date = text.strip()
                continue

            course_title = item.css("::text").get()
            course_url = item.css("a::attr(href)").get()

            if course_title and course_url:
                clean_title = course_title.strip().rstrip("–").rstrip("-").strip()

                course = CourseItem()
                course["title"] = clean_title
                course["url"] = course_url
                course["date"] = current_date if current_date else "Unknown"

                yield course
