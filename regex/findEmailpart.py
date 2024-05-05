import re
sente = "From Sandeep Gupta guptasandeep188@gmail.com Date:Apr 2, 2024, 7:57 PM"

extVal = re.findall('@([^ ]*)', sente)
extValFrom = re.findall('^From .*@([^ ]*)', sente) # more refine search
print(extVal) # ['gmail.com']
print(extValFrom) #['gmail.com']