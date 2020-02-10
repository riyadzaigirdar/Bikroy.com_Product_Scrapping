# -*- coding: utf-8 -*-
import scrapy


class BikroyProductSpider(scrapy.Spider):
    name = 'bikroy_product'
    allowed_domains = ['bikroy.com']
    page_number = 2
    start_urls = ['https://bikroy.com/bn/ads']

    
    def parse(self, response):
        top_ad = response.xpath("//li[@class='top-ads-container--1Jeoq gtm-top-ad']")
        for ad in top_ad:
            name = ad.xpath(".//span[@class='title--3yncE']/text()").get()
            place = ad.xpath(".//div[@class='description--2-ez3']/text()").get()
            price = ad.xpath(".//div[@class='price--3SnqI color--t0tGX']/span/text()").get()

            yield {
               'name' : name,
               'place' : place,
               'price' : price 
            }

        normal_add = response.xpath("//li[contains(@class,'normal--2QYVk gtm-normal-ad')]")
        for ad in normal_add:
            name = ad.xpath(".//span[@class='title--3yncE']/text()").get()
            place = ad.xpath(".//div[@class='description--2-ez3']/text()").get()
            price = ad.xpath(".//div[@class='price--3SnqI color--t0tGX']/span/text()").get()
            
            yield {
               'name' : name,
               'place' : place,
               'price' : price 
            }
        
        
        next_page = f'https://bikroy.com/bn/ads?by_paying_member=0&sort=date&order=desc&buy_now=0&page={self.page_number}'  
        
        if next_page:
            self.page_number += 1
            yield scrapy.Request(url=next_page,callback=self.parse)