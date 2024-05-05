import re;
fopen = open('../email.txt')

for data in fopen:
    stpData = data.rstrip()
    if(re.search('^From', stpData)): # ^ use to search starting with
        print(stpData) # From:Sandeep Gupta guptasandeep188@gmail.com