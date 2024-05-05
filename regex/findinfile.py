
import re
fopen = open('../email.txt')

lst = []
# Iterate through each line in the file
for line in fopen:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Use regular expression to find lines starting with "From"
    res = re.findall('^From:.+', line)
    
    # Append the result to the list
    lst.append(res)

# Print the list of matches
print(lst) #['From:Sandeep Gupta guptasandeep188@gmail.com']



