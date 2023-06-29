# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

# from pathlib import Path
import w3lib.html
import lotto_results.settings as settings
from lotto_results.items import LottoItem


class LottoSpider(scrapy.Spider):
    name = "lottos"
    allowed_domains = ["https://www.lottopcso.com/"]

    def start_requests(self):
        # Test run for start_request method alone
        user_input = [
            {"month": "June", "day": "19", "year": "2023"},
            {"month": "June", "day": "20", "year": "2023"},
            {"month": "June", "day": "22", "year": "2023"},
            {"month": "June", "day": "23", "year": "2023"},
            {"month": "June", "day": "24", "year": "2023"},
            {"month": "June", "day": "25", "year": "2023"},
            {"month": "June", "day": "26", "year": "2023"},
        ]
        urls = [
            f"https://www.lottopcso.com/pcso-lotto-result-{dates['month']}-{dates['day']}-{dates['year']}/"
            for dates in user_input
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table_row = response.css("table tr")

        draw_entry_1 = LottoItem()

        draw_entry_1["url"] = response.url
        draw_entry_1["draw"] = w3lib.html.remove_tags(
            table_row[1].xpath("//div[2]/figure[1]/table/thead/tr/th[1]").get()
        )
        draw_entry_1["winning_combination"] = w3lib.html.remove_tags(
            table_row[1].xpath("//div[2]/figure[1]/table/tbody/tr[1]/td[2]").get()
        )
        draw_entry_1["winning_value"] = w3lib.html.remove_tags(
            table_row[1].xpath("//div[2]/figure[1]/table/tbody/tr[2]/td[2]").get()
        )
        draw_entry_1["num_of_winners"] = w3lib.html.remove_tags(
            table_row[1].xpath("//div[2]/figure[1]/table/tbody/tr[3]/td[2]").get()
        )
        draw_entry_1["draw_date"] = response.css("span.post_date ::text").get()

        draw_entry_2 = LottoItem()

        draw_entry_2["url"] = response.url
        draw_entry_2["draw"] = w3lib.html.remove_tags(
            table_row[0].xpath("//div[2]/figure[2]/table/thead/tr/th[1]").get()
        )
        draw_entry_2["winning_combination"] = w3lib.html.remove_tags(
            table_row[0].xpath("//div[2]/figure[2]/table/tbody/tr[1]/td[2]").get()
        )
        draw_entry_2["winning_value"] = w3lib.html.remove_tags(
            table_row[0].xpath("//div[2]/figure[2]/table/tbody/tr[2]/td[2]").get()
        )
        draw_entry_2["num_of_winners"] = w3lib.html.remove_tags(
            table_row[0].xpath("//div[2]/figure[2]/table/tbody/tr[3]/td[2]").get()
        )
        draw_entry_2["draw_date"] = response.css("span.post_date ::text").get()

        draws = [draw_entry_1, draw_entry_2]
        for draw in draws:
            yield draw

        # For debugging
        # url = response.url
        # first_draw = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[1]/table/thead/tr/th[1]").get()
        # )
        # first_winning_combination = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[1]/table/tbody/tr[1]/td[2]").get()
        # )
        # first_jackpot_prize = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[1]/table/tbody/tr[2]/td[2]").get()
        # )
        # first_num_of_winners = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[1]/table/tbody/tr[3]/td[2]").get()
        # )
        # date = response.css("span.post_date ::text").get()

        # second_draw = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[2]/table/thead/tr/th[1]").get()
        # )
        # second_winning_combination = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[2]/table/tbody/tr[1]/td[2]").get()
        # )
        # second_jackpot_prize = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[2]/table/tbody/tr[2]/td[2]").get()
        # )
        # second_num_of_winners = w3lib.html.remove_tags(
        #     table_row[0].xpath("//div[2]/figure[2]/table/tbody/tr[3]/td[2]").get()
        # )

        # first_draw = {
        #     "url": url,
        #     "draw": first_draw,
        #     "winning combination": first_winning_combination,
        #     "jackpot prize": first_jackpot_prize,
        #     "num of winners": first_num_of_winners,
        #     "date": date,
        # }

        # second_draw = {
        #     "url": url,
        #     "draw": second_draw,
        #     "winning combination": second_winning_combination,
        #     "jackpot prize": second_jackpot_prize,
        #     "num of winners": second_num_of_winners,
        #     "date": date,
        # }

        # draws = [first_draw, second_draw]
        # for draw in draws:
        #     yield draw
