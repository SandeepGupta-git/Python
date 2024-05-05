
fop = open('email.txt')
dictionary = dict()

for words in fop:
    each_word = words.split()
    # print(each_word)
    for word in each_word:
        dictionary[word] = dictionary.get(word, 0) + 1
print(dictionary)
lst = list()
for k, v in dictionary.items():
    lst.append((v, k))
lst = sorted(lst, reverse=True) # can sort tuple not dictionary
for v, k in lst[:10]:
    print(k, v)