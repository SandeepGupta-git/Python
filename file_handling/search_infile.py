fopen = open('test_mail.txt')
    # Iterate through each line in the file
for line in fopen:
        # Check if the line starts with "From:"
        if line.startswith('From:'):
            # If found, print the line
            print(line.strip())
            break
        if not line in fopen:
            print('From Not Found')
print('End of file')