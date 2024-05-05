
fopen = open('email.txt')

dic= dict()
for words in fopen:
    each_word = words.split()
    for word in each_word:
        dic[word] = dic.get(word, 0) + 1
sor = sorted( [ (v, k) for k, v in dic.items() ], reverse= True )

print(sor[:10])  
