from datetime import datetime
from urllib.parse import ParseResult

print(datetime.now())
current_time=(datetime.now())
print(current_time)
format1=current_time.strftime("%Y-%m-%d-%H:%M:%S")
print(format1)
format2=current_time.strftime("%m/%d/%y")
print(format2)
format3=current_time.strftime("%A,%m,%d,%Y")
print(format3)
format4=current_time.strftime("%A,%m,%d,%y %H:%M:%S %p")
print(format4)
format5=current_time.strftime("%a-%b-%d %H:%M:%S %z %Y")
print(format5)
format6=current_time.strftime("a-%b-%d %H:%M:%S %z %Y")
print(format6)
