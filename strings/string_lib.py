
# lower case
msg = "good Morning Dear"

print(msg.lower()) # good morning dear

# upper case

print(msg.upper()) # GOOD MORNING DEAR

# capitalize

print('--', msg.capitalize()) # Good Morning Dear

# all sting built in functions
type(msg)
print(dir(msg))

##
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

##

# find

findthis = msg.find('Dear')
print('found', findthis) # 13 (returns index value of first occurance)

# replace

msg2 = msg.replace('Dear' , 'Baby')
print('new Msg', msg2) # good Morning Baby

# remove extra spaces

spaces = '   this has useless spaces in start and end    '
print(spaces.lstrip())
print(spaces.rstrip())
print(spaces.strip())

# startwith

print(msg.startswith('good')) # true