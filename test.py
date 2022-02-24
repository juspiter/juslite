import datetime
import time

_data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
br_data = time.strftime("%d/%m/%Y %H:%M", time.localtime())
utc_data = time.strftime("%d/%m/%Y %H:%M", time.gmtime())

print ("N------>" + _data)
print ("BR----->" + br_data)
print ("UTC---->" + utc_data)
