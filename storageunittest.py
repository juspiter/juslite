import unittest
from storage import Storage


class TestStorage(unittest.TestCase):
    conn = Storage('172.17.0.3:27017')

    def test_if_storage_return_mongo_client(self):
        self.assertIsNotNone(self.conn)

    def test_method_get_lawsuit(self):
        response = self.conn.get_lawsuit()
        self.assertIsNotNone(response)
