
smallest = None
for i in [2,21,33,44,1]:
    if smallest is None:
        smallest = i
        print(smallest)
    elif i < smallest:
        smallest = i
        print(smallest)
print('smallest', smallest)