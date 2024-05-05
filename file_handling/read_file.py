
fileName = open('test_mail.txt')
readFile = fileName.read()
print(readFile)
print(len(readFile)) # 953 (total No of Char)

print(readFile[:45]) # From:Sandeep Gupta <guptasandeep188@gmail.com