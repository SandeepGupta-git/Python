
fruit = {'mango' : 100, 'banana': 80, 'grapes': 120}
lst = list()
for k, v in fruit.items():
    lst.append((k,v))
    print(lst)
    sortedByPrice = sorted(lst, reverse=True)
    print(sortedByPrice) #[('mango', 100), ('grapes', 120), ('banana', 80)]