from suitparser import SuitParser
import unittest

class TestSuitParser(unittest.TestCase):
    def test_00_all_is_number(self):
        str_num = "0000001-02.2017.8.02.0149"
        ret = SuitParser(str_num)
        self.assertTrue(ret.is_valid)

    def test_01_receives_formatted_number_and_returns_without_change(self):
        str_num = "0000001-02.2017.8.02.0149"
        ret = SuitParser(str_num)
        self.assertEqual(str_num, ret.formatted_number)

    def test_02_return_true_when_number_is_valid(self):
        str_num = "0000001-02.2017.8.02.0149"
        ret = SuitParser(str_num)
        self.assertTrue(ret.is_valid)

    def test_03_return_true_when_number_is_valid_but_not_formatted(self):
        str_num = "00000010220178020149"
        ret = SuitParser(str_num)
        self.assertTrue(ret.is_valid)

    def test_04_return_false_when_number_is_shorter_than_valid(self):
        str_num = "666" # roque _|m/ 😈
        ret = SuitParser(str_num)
        self.assertFalse(ret.is_valid)

    def test_05_return_format_number_from_raw_number(self):
        str_num = "00000010220178020149"
        ret = SuitParser(str_num)
        formatted_number = ret.formatted_number
        self.assertEqual("0000001-02.2017.8.02.0149", formatted_number)

    def test_06_return_false_because_there_are_letters(self):
        str_num = "0710x02-55.2018.8.02.0001"
        ret = SuitParser(str_num)
        self.assertFalse(ret.is_valid)

    def test_07_return_false_if_court_is_not_supported(self):
        ret = SuitParser("0000001-02.2017.6.02.0149")
        self.assertFalse(ret.is_valid)

    def test_08_return_false_if_court_is_not_supported2(self):
        ret = SuitParser("0000001-02.2017.8.03.0149")
        self.assertFalse(ret.is_valid)

    def test_09_return_false_if_future_prediction(self):
        ret = SuitParser("0000001-02.2077.8.02.0149")
        self.assertFalse(ret.is_valid)
