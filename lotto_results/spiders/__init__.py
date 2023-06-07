# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from pathlib import Path

import scrapy


class LottoSpider(scrapy.Spider):
    name = "lottos"
    allowed_domains = ["https://www.lottopcso.com/"]

    def start_requests(self, user_input: list[dict]):
        # Test run for start_request method alone
        # user_input = [
        #     {"month": "April", "day": "24", "year": "2017"},
        #     {"month": "August", "day": "8", "year": "2016"},
        #     {"month": "July", "day": "14", "year": "2021"},
        # ]
        urls = [
            f"https://www.lottopcso.com/pcso-lotto-result-{dates['month']}-{dates['day']}-{dates['year']}/"
            for dates in user_input
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"logs/{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file logs/{filename}")
