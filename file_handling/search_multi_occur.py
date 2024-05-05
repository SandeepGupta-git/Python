
openFile = open('test_mail.txt')

for i in openFile:
    if i.startswith('From:'):
        print(i)
        
    if not i.startswith('From:'):
        continue
print('EOF')