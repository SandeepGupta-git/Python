
opn = open('email.txt')
count = dict()
for words in opn:
    eachWord = words.split()
    for countWord in eachWord: 
        count[countWord] = count.get(countWord, 0) + 1
    

lst = list()
for k,v in count.items(): 
    lst.append((v,k))

lst = sorted(lst, reverse=True)
for v, k in lst[:10]:
    print(k,v)
   