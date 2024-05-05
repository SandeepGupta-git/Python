counts =  dict()
inpt = input('Enter sentance')

strings = inpt.split()

print(strings) #['this', 'is', 'a', 'very', 'long', 'story', 'of', 'a', 'villabe', 'where', 'a']

for vals in strings:
    counts[vals] = counts.get(vals, 0) + 1

print(counts) # {'this': 1, 'is': 1, 'a': 3, 'very': 1, 'long': 1, 'story': 1, 'of': 1, 'villabe': 1, 'where': 1}