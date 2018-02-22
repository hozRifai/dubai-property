# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FinalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ProjID = scrapy.Field()
    ProjectName = scrapy.Field()
    StartingPrice = scrapy.Field()
    PricePerSqftfrom  = scrapy.Field()
    AreaFrom  = scrapy.Field()
    Type  = scrapy.Field()
    Bedrooms  = scrapy.Field()
    Location  = scrapy.Field()
    Developer  = scrapy.Field()
    PaymentPlan  = scrapy.Field()

class PaymentPlan(scrapy.Item):
    installment = scrapy.Field()
    milestone   = scrapy.Field()
    percentage  = scrapy.Field()
    PaymentID = scrapy.Field()
class PaymentId(scrapy.Item):
    PaymentID   = scrapy.Field()
class Counter(scrapy.Field):
    Counter     = scrapy.Field()