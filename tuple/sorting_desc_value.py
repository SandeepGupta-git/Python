
fruit = {'mango' : 100, 'banana': 80, 'grapes': 120}
lst = list() #collection
for k, v in fruit.items():
    lst.append((v,k)) #tuple
    print(lst)
    sortedByPrice = sorted(lst, reverse=True)
    print(sortedByPrice) #[(120, 'grapes'), (100, 'mango'), (80, 'banana')]