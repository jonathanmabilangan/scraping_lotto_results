# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

# from pathlib import Path
import w3lib.html
from lotto_results.items import LottoItem


class LottoSpider(scrapy.Spider):
    name = "lottos"
    allowed_domains = ["https://www.lottopcso.com/"]

    def start_requests(self):
        # Test run for start_request method alone
        user_input = [
            {"month": "April", "day": "24", "year": "2022"},
            {"month": "February", "day": "10", "year": "2023"},
            {"month": "July", "day": "14", "year": "2021"},
        ]
        urls = [
            f"https://www.lottopcso.com/pcso-lotto-result-{dates['month']}-{dates['day']}-{dates['year']}/"
            for dates in user_input
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table_row = response.css("table tr")

        draw_entry = LottoItem()

        draw_entry["url"] = response.url
        draw_entry["draw"] = w3lib.html.remove_tags(
            table_row[1].xpath("//div[2]/figure[1]/table/thead/tr/th[1]/strong").get()
        )
        draw_entry["winning_combination"] = w3lib.html.remove_tags(
            table_row[1].xpath("//div[2]/figure[1]/table/tbody/tr[1]/td[2]").get()
        )
        draw_entry["winning_value"] = w3lib.html.remove_tags(
            table_row[1].xpath("//div[2]/figure[1]/table/tbody/tr[2]/td[2]").get()
        )
        draw_entry["num_of_winners"] = w3lib.html.remove_tags(
            table_row[1].xpath("//div[2]/figure[1]/table/tbody/tr[3]/td[2]").get()
        )
        draw_entry["draw_date"] = response.css("span.post_date ::text").get()

        # url = response.url
        # draw = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[1]/table/thead/tr/th[1]/strong").get()
        # )
        # winning_combination = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[1]/table/tbody/tr[1]/td[2]").get()
        # )
        # jackpot_prize = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[1]/table/tbody/tr[2]/td[2]").get()
        # )
        # num_of_winners = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[1]/table/tbody/tr[3]/td[2]").get()
        # )
        # date = response.css("span.post_date ::text").get()

        # yield {
        #     "URL": url,
        #     "Draw": draw,
        #     "Result": winning_combination,
        #     "Jackpot Prize": jackpot_prize,
        #     "Number of Winner/s": num_of_winners,
        #     "Date": date,
        # }

        # print(url, draw, winning_combination, jackpot_prize, num_of_winners, date)

        yield draw_entry
