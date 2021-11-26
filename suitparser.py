import datetime


class SuitParser:
    def __init__(self, number: str):
        self.number = number
        self.is_valid = self.check_number(self.number)
        if self.is_valid is False:
            return
        self.formatted_number = self.format_number(self.number)

    def check_number(self, number: str) -> bool:
        raw_num = number.translate({ord(c): None for c in '.-'})
        if (len(raw_num) != 20 or not
            raw_num.isdigit() or not
            self.court_is_valid(raw_num) or not
            self.year_is_valid(raw_num)):
            return False
        self.number = raw_num
        return True

    def court_is_valid(self, raw_num: str) -> bool:
        if raw_num[13] == '8' and raw_num[14:16] in ['02', '06']:
            return True
        return False

    def year_is_valid(self, raw_num: str) -> bool:
        current_year = datetime.datetime.now().year
        return True if current_year >= int(raw_num[9:13]) else False

    def format_number(self, n: str) -> str:
        return f"{n[:7]}-{n[7:9]}.{n[9:13]}.{n[13]}.{n[14:16]}.{n[16:]}"
