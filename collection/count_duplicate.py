
names = ['mango','banana','grape','mango']
count = dict()
for itm in names:
    if itm not in count:
        count[itm] =  1
    else:
        count[itm] = count[itm] + 1
print(count) # {'mango': 2, 'banana': 1, 'grape': 1}

# === same we can do usin get() =============
fnames = ['mango','banana','grape','mango']
fcount = dict()
for pdt in fnames:
    fcount[pdt] = fcount.get(pdt, 0) + 1
print('--', fcount) # {'mango': 2, 'banana': 1, 'grape': 1}
#####===========================================
#count = dict() # not required cause below is arady dictionary.
fname2 = { 'quincy' : 3 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(fname2.get('quincy', 100)) # key , default value - output - 3 (cause value already given)
#####==========================================
fname3 = { 'quincy' : 3 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(fname3.get('Kris', 100)) # 100