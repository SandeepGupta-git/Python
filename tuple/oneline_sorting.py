fruit = {'mango' : 100, 'banana': 80, 'grapes': 120}

print(sorted([ (v,k ) for k, v in fruit.items()], reverse=True))

# above code equal to below
lst = []
for key, val in fruit.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)