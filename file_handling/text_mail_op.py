
# open text file

openEmailTxt = open('test_mail.txt')
print('--', openEmailTxt) # -- <_io.TextIOWrapper name='test_mail.txt' mode='r' encoding='cp1252'>
printLineNumber = 0
for printline in openEmailTxt:
    printLineNumber = printLineNumber + 1
    print(printLineNumber , '.' , printline)
print('Total Lines =', printLineNumber)


