# -*- coding: utf-8 -*-
import scrapy
from final.items import PaymentPlan
from final.items import PaymentId
from final.items  import Counter
class PaymentplanSpider(scrapy.Spider):
    name = 'paymentPlan'
    allowed_domains = ['dxboffplan.com']
    start_urls = ['https://dxboffplan.com/property-for-sale-dubai/']
    custom_settings = {
        'FEED_EXPORT_FIELDS': ["PaymentID"  , "installment" , "percentage" , "milestone"],
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
        InstallmentValidation = ["1st Installment" , "2nd Installment" , "3rd Installment" , "4th Installment" , "5th Installment" ,
                                 "6th Installment" , "7th Installment" , "8th Installment" , "9th Installment" , "10th Installment" ,
                                 "11th Installment" , "12th Installment", "13th Installment" , "14th Installment" , "15th Installment" ,
                                 "16st Installment", "17nd Installment", "18rd Installment", "19th Installment","20th Installment","21th Installment", "7th Installment", "8th Installment", "9th Installment",
                                 "22th Installment", "23th Installment", "24th Installment", "25th Installment", "26th Installment",
                                 "27th Installment", "28st Installment" , "29nd Installment" , "30rd Installment" , "31th Installment" ,
                                 "32th Installment" ,
                                 "33th Installment" , "34th Installment" , "35th Installment" , "36th Installment" , "37th Installment" ,
                                 "38th Installment" , "39th Installment", "40th Installment" , "41th Installment" , "42th Installment" ,
                                 ]
        var = PaymentPlan()
        let = PaymentId()
        const = Counter()
        a = response.css('div.project-metas > h1::text').extract_first()
        variable = a.split(" ")
        b = variable[0] + variable[1]
        if response.css('div.project-content  table tr'):
            let["PaymentID"] = b + "_Plan"
            yield let
        """def countMe(counter=[0]):
            counter[0] += 1
            print(counter[0])"""
        for item in response.css('div.project-content  table tr'):
            #const["Counter"] = countMe()
            var["installment"] = item.css(' td::text').extract_first()
            var["percentage"]  = item.css('td:nth-child(n+3)::text').extract_first()
            var["milestone"]   = item.css('td:nth-child(n+2)::text').extract_first()
            if var['installment'] is None:
                del var['installment']
            if var['milestone'] is None:
                del var['milestone']
            if var['percentage'] is None:
                del var['percentage']
            if "installment" in var:
                if var['installment'].isdigit():
                    var['installment'] = "Payment" +  var['installment']
                if  var['installment']  in InstallmentValidation:
                    if "&nbsp;" in var['installment']:
                        var['installment'] = var['installment'].replace("&nbsp;" , " ")
                    numbersFP  = var['installment'].split(" ") # FP= first phase
                    FirstNumber = numbersFP[0][:-2]
                    var['installment'] = "Payment" + FirstNumber
                yield var