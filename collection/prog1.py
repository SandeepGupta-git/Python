

lists = list()
while True:
    x = input('enter number ') # reading in strin type cause all input are treated as string
    if x == 'done': break
    value = float(x) # or convert in integer
    lists.append(x)

avg = sum(lists) / len(lists)
print(avg)