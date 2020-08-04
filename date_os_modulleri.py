from datetime import datetime

suan = datetime.today()

result = suan.month
print(result)

result = datetime.strftime(suan,"%Y %B %A") 

print(result, "\n")


import os       # operating system modulu buradan dizini goruntuleyip yolunu degistirebilirsin

s = dir(os)

print(s)



