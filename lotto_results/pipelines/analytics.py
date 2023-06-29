from itemadapter import ItemAdapter
from datetime import datetime
import mysql.connector
import lotto_results.settings as settings


class GetDayResultLotto:
    def __init__(self) -> None:
        try:
            self.conn = mysql.connector.connect(
                host=settings.HOST,
                user=settings.DB_USER,
                password=settings.PASSWORD,
                database=settings.DATABASE,
            )

            self.cur = self.conn.cursor()

        except ConnectionError as conerror:
            raise conerror

    def select_items(self, items, draw, from_date, to_date):
        draw = "6/"
        items = self.cur.execute(
            """
            SELECT winning_combination 
            FROM lotto_result
            WHERE draw = %s
            AND draw_date >= %s
            AND draw_date <= %s""",
            (draw, from_date, to_date),
        )
        self.conn.commit()
        return items

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
