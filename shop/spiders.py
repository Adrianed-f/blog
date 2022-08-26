from decimal import Decimal

import scrapy


class OmaSpider(scrapy.Spider):
    name = "oma.by"
    start_urls = ["https://www.oma.by/elektroinstrument-c"]

    def parse(self, response, **kwargs):
        for product in response.css(".catalog-grid .product-item"):
            cost = product.css(".product-price-block .price__normal::text").get().strip()
            data = {
                "external_id": product.attrib.get("data-ga-product-id"),
                "title": product.css(".product-title-and-rate-block .wrapper::text").get().strip(),
                "cost": Decimal(cost.replace(',', '.')),
                "link": f"https://oma.by{product.css('a.area-link::attr(href)').get()}",
            }
            yield data

        next_page = response.css(".page-nav_box .btn__page-nav:last-child::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

