# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

from pathlib import Path
import w3lib.html


class LottoSpider(scrapy.Spider):
    name = "lottos"
    allowed_domains = ["https://www.lottopcso.com/"]

    def start_requests(self):
        # Test run for start_request method alone
        user_input = [
            {"month": "April", "day": "24", "year": "2022"},
            {"month": "January", "day": "8", "year": "2023"},
            {"month": "July", "day": "14", "year": "2021"},
        ]
        urls = [
            f"https://www.lottopcso.com/pcso-lotto-result-{dates['month']}-{dates['day']}-{dates['year']}/"
            for dates in user_input
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"logs/{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file logs/{filename}")
        # for row in response.xpath('//*[@id="post-******"]/div[2]/figure[1]'):
        for row in response.xpath('//*[contains(@class, "has-fixed-layout")]'):
            # filename = f"logs/{row}.html"
            # Path(filename).write_bytes(response.body)
            # self.log(f"{row}")
            # print(f"someone {row.css('td::text').get()}")
            # print(f"headers {row.css('th::text').get()}")
            draw = w3lib.html.remove_tags(row.xpath(".//strong").get())
            result = w3lib.html.remove_tags(row.xpath(".//td")[1].get())

            print(f"Lotto:{draw}, Result: {result}")
