#co = dict() only use when data is collection means inside [], below is already a dictionary
data = { 'quincy' : 3 , 'mrugesh' : 42, 'beau': 100, '0': 10}

for key in data:
    print(key, data[key])

# dictionary methods

print('1',list(data)) #['quincy', 'mrugesh', 'beau', '0']

print(data.keys()) # dict_keys(['quincy', 'mrugesh', 'beau', '0'])


print(data.values()) # dict_values([3, 42, 100, 10])

print(data.items()) # dict_items([('quincy', 3), ('mrugesh', 42), ('beau', 100), ('0', 10)])

