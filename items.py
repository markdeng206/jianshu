# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    article_title = scrapy.Field()
    aricle_content = scrapy.Field()
    article_id = scrapy.Field()
    origin_url = scrapy.Field()
    article_author = scrapy.Field()
    article_avatar = scrapy.Field()
    article_pubTime = scrapy.Field()
    read_count=scrapy.Field()
    word_count=scrapy.Field()
    subjects=scrapy.Field()
    comment_count=scrapy.Field()
    like_count=scrapy.Field()
