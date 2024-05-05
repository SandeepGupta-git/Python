
emailstring = 'bob_t_rogan@gmail.com is the mail id of CEO'

findattherate = emailstring.find('@')
print(findattherate)

findspace = emailstring.find(' ', findattherate)

emailis = emailstring[findattherate+1:findspace]

print('email is', emailis)