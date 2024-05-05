
x = (1,2,3,4,0)
print(x[3]) # 4
print(x.sort()) # AttributeError: 'tuple' object has no attribute 'sort'
print(x.append(3)) # AttributeError: 'tuple' object has no attribute 'sort'

(m,b) = ('Mongo', 'Banana')
print(m,b) # Mango Banana

m = ('Grapes') # or m = 'Grapes
print(m,b) # Grapes Banana

print((1,2,3) < (1,3,0)) # True . it will compare one by one and return the result and doesnot go further.
print((1,22,3) < (1,3,10)) # False . it will compare one by one and return the result and doesnot go further.


dic = dict()
dic['Mango'] = 200
dic['Banana'] = 60
#using list/collection only key
for key in dic:
    print(key, dic[key])
# using lists/collection
for key, val in dic.items() :
    print(key, val)
#using tuple
for (key, val) in dic.items():
    print(key, val)

#output - Mango 200
#         Banana 60
