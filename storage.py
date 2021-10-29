from pymongo import MongoClient


class Storage:
    def __init__(self, addr):
        self.conn = MongoClient(addr, serverSelectionTimeoutMS=5000)
        try:
            self.conn.server_info()
        except ServerSelectionTimeoutError:
            self.conn = None

    def get_lawsuit(self):
        return self.conn.jusdb.lawsuits.find_one()
