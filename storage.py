from pymongo import MongoClient, errors


class Storage:
    def __init__(self, addr: str):
        self.conn = MongoClient(addr, serverSelectionTimeoutMS=5000)
        try:
            self.conn.server_info()
        except errors.ServerSelectionTimeoutError:
            self.conn = None

    def add_lawsuit(self, lawsuit: dict):
        if lawsuit == {}:
            return
        num = lawsuit['number']
        self.conn.jusdb.lawsuits.find_one_and_update(
            {"number": num}, {'$set': lawsuit}, upsert=True)

    def get_lawsuit(self, number:str) -> dict:
        return self.conn.jusdb.lawsuits.find_one({"number": number})

    def delete_lawsuit(self, number: str):
        self.conn.jusdb.lawsuits.delete_one({"number": number})

    def count_lawsuits(self) -> int:
        return self.conn.jusdb.lawsuits.count_documents({})
