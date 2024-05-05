dic = {
    'fruit_name' : 'mango',
    'fruit_price' : 100,
    'availability': True
}

print(dic['fruit_price'] + 20) # 120
#dic = dict()
dic['availability'] = False
dic['season'] = 'summer'
print(dic) # {'fruit_name': 'mango', 'fruit_price': 100, 'availability': False, 'season': 'summer'}
