# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class JugamosotraPipeline:
    def __init__(self):
        self.con = sqlite3.connect(
            'C:/Users/u10054206/OneDrive - NOS SGPS, S.A/Carreira/Portfolio/Python Projects/Scrapy/boardgames/boardgames.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS jugamosotra(
        id REAL,
        name VARCHAR(100),
        price FLOAT,
        availability VARCHAR(100),
        url VARCHAR(255),
        bgg_url VARCHAR(255),
        date DATE
        )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO jugamosotra VALUES (?,?,?,?,?,?,?)""",
                         (item['id'], item['name'], item['price'], item['availability'],
                          item['url'], item['bgg_url'], item['date']))
        self.con.commit()
        return item
