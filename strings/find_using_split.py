
file = open('../email.txt')

for i in file:
    i.strip() # removing space from start and end
    if not i.startswith('From'):
        continue
    itm = i.split() 
    print(itm) #['From:Sandeep', 'Gupta', '<guptasandeep188@gmail.com>']
    print(itm[2]) # <guptasandeep188@gmail.com>

    mailService = itm[2]
    sp = mailService.split('@')
    
    print('service provider', sp[1]) #gmail.com

   
    



