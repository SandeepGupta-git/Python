
file = input('enter file path and name')
handle = open(file)

dic = dict()
for words in handle:
    slicing = words.split()
    for countword in slicing:
        dic[countword] = dic.get(countword, 0) + 1

print(dic)