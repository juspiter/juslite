from pymongo import MongoClient


class Storage:
    def __init__(self, addr: str):
        self.conn = MongoClient(addr, serverSelectionTimeoutMS=5000)
        try:
            self.conn.server_info()
        except ServerSelectionTimeoutError:
            self.conn = None

    def add_lawsuit(self):
        self.conn.jusdb.lawsuits.insert_one({
            "number": "0710802-55.2018.8.02.0001",
            "changes":
            [
                {
                    "date": "22/02/2021",
                    "title": "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso",
                    "content": ""
                },
                {
                    "date": "10/02/2021",
                    "title": "Juntada de Documento",
                    "content": "Nº Protocolo: WMAC.21.70031538-2 Tipo da Petição: Contrarrazões Data: 10/02/2021 19:27"
                }
            ]
    })

    def get_lawsuit(self) -> dict:
        return self.conn.jusdb.lawsuits.find_one()

    def delete_lawsuit(self):
        self.conn.jusdb.lawsuits.delete_one({})

    def count_lawsuits(self) -> int:
        return self.conn.jusdb.lawsuits.count_documents({})
