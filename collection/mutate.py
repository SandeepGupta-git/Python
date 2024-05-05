

# fruit = 'mango' # ['m','a','n','g','o']
# fruit[0] = 'M'
# print(fruit)

fruits = ['Mango','banana']

for fruitNames in fruits:
    print('1',fruits)
    fruits[1] = 'papaya'
    print('2',fruits)
    if(fruitNames == 'papaya'):
        fruits[1] = 'grapes'
        print('3',fruits)

vegi = ['potato','tomamto','flower']

print(len(vegi)) # 3
print(range(len(vegi))) # range(0,2)
# print(range(fruits))
