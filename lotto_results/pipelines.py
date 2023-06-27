# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
import mysql.connector
import lotto_results.settings as settings


class LottoResultsPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        winning_value = adapter.get("winning_value")
        winning_value = winning_value.replace(winning_value[:4], "")
        winning_value = winning_value.replace(",", "")
        adapter["winning_value"] = winning_value

        string_to_date = datetime.strptime(adapter["draw_date"], "%B %d, %Y")
        adapter["draw_date"] = datetime.strftime(string_to_date, "%Y-%m-%d")

        return item


class SaveToDBPipeline:
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(
            host=settings.HOST,
            user=settings.DB_USER,
            password=settings.PASSWORD,
            database=settings.DATABASE,
        )

        self.cur = self.conn.cursor()

        # Create table if it does not exist

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS lotto_result(
              id INT NOT NULL auto_increment,
              url VARCHAR(255),
              draw VARCHAR(255),
              winning_combination VARCHAR(50),
              winning_value DECIMAL,
              num_of_winners INTEGER,
              draw_date DATE,
              PRIMARY KEY (id)
            )
        """
        )

    def process_item(self, item, spider):
        # Insert statement
        self.cur.execute(
            """
            INSERT into lotto_result(
            url, 
            draw,
            winning_combination,
            winning_value,
            num_of_winners,
            draw_date)
            values(
              %s, %s,
              %s, %s,
              %s, %s)""",
            (
                item["url"],
                item["draw"],
                item["winning_combination"],
                item["winning_value"],
                item["num_of_winners"],
                item["draw_date"],
            ),
        )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
