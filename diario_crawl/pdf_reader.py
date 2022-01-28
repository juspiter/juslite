import PyPDF4
import re

FILE_PATH = './Caderno2-Jurisdicional-PrimeiroGrau.pdf'

with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF4.PdfFileReader(f)
    page = reader.getPage(0)
    txt = page.extractText().replace('\n', '')
    
    lawsuit_list = re.findall("[0-9]{7}\-[0-9]{2}\.[0-9]{4}\.8\.02\.[0-9]{4}", txt)


# stringa = "0000001-29.2014.8.02.0077 aaaaaaaaaaaaaa"
# regex_ret = re.findall("[0-9]{7}\-[0-9]{2}\.[0-9]{4}\.[0-9]\.[0-9]{2}\.[0-9]{4}", stringa)
    # print(txt)
    print(lawsuit_list)
    
    # 0000001-29.2014.8.02.0077