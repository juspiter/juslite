from pymongo import MongoClient


class Storage:
    def __init__(self, addr: str):
        self.conn = MongoClient(addr, serverSelectionTimeoutMS=5000)
        try:
            self.conn.server_info()
        except ServerSelectionTimeoutError:
            self.conn = None

    def add_lawsuit(self, lawsuit: dict):
        num = lawsuit['number']
        self.conn.jusdb.lawsuits.find_one_and_update(
            {"number": num}, {'$set': lawsuit}, upsert=True)

    def get_lawsuit(self) -> dict:
        return self.conn.jusdb.lawsuits.find_one()

    def delete_lawsuit(self):
        self.conn.jusdb.lawsuits.delete_one({})

    def count_lawsuits(self) -> int:
        return self.conn.jusdb.lawsuits.count_documents({})
