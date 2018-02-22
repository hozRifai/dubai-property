# -*- coding: utf-8 -*-
import scrapy
from final.items  import FinalItem
class FinalReleaseSpider(scrapy.Spider):
    name = 'final_release'
    allowed_domains = ['dxboffplan.com']
    start_urls = ['https://dxboffplan.com/property-for-sale-dubai/']
    custom_settings = {
        'FEED_EXPORT_FIELDS': ["ProjID" , "ProjectName", "StartingPrice" , "PricePerSqftfrom" , "AreaFrom" ,"Type" ,"Bedrooms" , "Location" ,  "Developer" , "PaymentPlan" ],
    }
    def parse(self, response):
        # get the urls of each property
        urls = response.css('div.property-listing > a::attr(href)').extract()
        # for each property make a request to get the details of each property
        for url in urls:
            yield scrapy.Request(url = url , callback = self.parse_details )
        # go and get the link for the next property
        next_page = response.css('div.property-listing > a::attr(href)').extract_first()
        # to get the details of the property we go throught a life cycle !
        yield scrapy.Request(url = next_page , callback = self.parse )

    def parse_details(self, response):
        var = FinalItem()
        var["ProjectName"]          = response.css('div.project-metas > h1::text').extract_first()
        variable                    = var["ProjectName"].split(" ")
        var["ProjID"]                = variable[0] + variable[1]
        var["StartingPrice"]        = response.css('table.project-table tr td::text').extract_first()
        var["PricePerSqftfrom"]     = response.css('table.project-table tr td::text').extract_first()
        var["AreaFrom"]             = response.css('table.project-table tr td::text').extract_first()
        a                           = response.css('table.project-table tr td a::text').extract()
        var["Type"]                 = a[0]
        var["Bedrooms"]             = response.css('table.project-table tr td span::text').extract()
        var["Location"]             = a[1]
        var["Developer"]            = a[2]
        var["PaymentPlan"]          = var["ProjID"] + "_Plan"
        yield var

