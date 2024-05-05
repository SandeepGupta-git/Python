str1 = "hello string" # ['h','e','l','l','o',' ','s','t','r','i','n','g']
                      #   0   1   2   3   4   5   6   7  8   9  10  11

str2 = str1[0:7]  
print('sliced', str2) # hello s (not 't' 0-7 excluding 7)
str3 = str1[6:21]
print('long slice', str3) # string

# passing only one range

str4 = str1[:6]
print('str4', str4) # hello 


str5 = str1[6:] 
print('str5', str5) # string


str6 = str1[:] 
print('str6', str6) # hello string



