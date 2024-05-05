
string = "this is a message havin number 786"
string2 = "From abc@gmail.com this is a regular exxression topic @gmail"

import re

res = re.findall('[0-9]+', string)
print(res) # ['786']

res2 = re.findall(('\S+@\S+'), string2)
print(res2) # ['abc@gmail.com']

res3 = re.findall('^F.+?..', string2)
print(res3) # ['From']
