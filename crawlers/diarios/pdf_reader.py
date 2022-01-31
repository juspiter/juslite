import PyPDF4
import re
import sys

FILE_PATH = f'{sys.argv[1]}.pdf'

with open(FILE_PATH, mode='rb') as f:
    lawsuit_list = []

    reader = PyPDF4.PdfFileReader(f)

    for pagen in range(0, reader.numPages):
        page = reader.getPage(pagen)
        txt = page.extractText().replace('\n', '')
        lawsuit_list += re.findall("[0-9]{7}\-[0-9]{2}\.[0-9]{4}\.[0-9]\.[0-9]{2}\.[0-9]{4}", txt)

    lawsuit_list = list(dict.fromkeys(lawsuit_list))

with open(f"../{sys.argv[1]}_processos.csv", mode='w') as f:
    for line in lawsuit_list:
        f.write(line + '\n')
